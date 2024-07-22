export default function updateUniqueItems(groceryMap) {
  if (!(groceryMap instanceof Map)) {
    throw new Error('Cannot process');
  }
  for (const key of groceryMap.keys()) {
    if (groceryMap.get(key) === 1) {
      groceryMap.set(key, 100);
    }
  }
}
