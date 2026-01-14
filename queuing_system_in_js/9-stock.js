import express from 'express';
import { createClient } from 'redis';

const app = express();
const PORT = 1245;

/* -------------------- Redis client -------------------- */
const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

(async () => {
  await client.connect();
})();

/* -------------------- Data -------------------- */
const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

/* -------------------- Data access -------------------- */
const getItemById = (id) => {
  return listProducts.find((product) => product.id === id);
};

/* -------------------- Redis helpers -------------------- */
const reserveStockById = async (itemId, stock) => {
  await client.set(`item.${itemId}`, stock);
};

const getCurrentReservedStockById = async (itemId) => {
  const stock = await client.get(`item.${itemId}`);
  return stock ? parseInt(stock, 10) : 0;
};

/* -------------------- Routes -------------------- */

// List all products
app.get('/list_products', (req, res) => {
  const products = listProducts.map((product) => ({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
  }));

  res.json(products);
});

// Product details with current stock
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const reservedStock = await getCurrentReservedStockById(itemId);
  const currentQuantity = product.stock - reservedStock;

  res.json({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
    currentQuantity,
  });
});

// Reserve product
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const reservedStock = await getCurrentReservedStockById(itemId);

  if (reservedStock >= product.stock) {
    return res.json({
      status: 'Not enough stock available',
      itemId,
    });
  }

  await reserveStockById(itemId, reservedStock + 1);

  return res.json({
    status: 'Reservation confirmed',
    itemId,
  });
});

/* -------------------- Server -------------------- */
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
