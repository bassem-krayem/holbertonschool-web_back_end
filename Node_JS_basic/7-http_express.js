const express = require('express');
const fs = require('fs').promises;

const app = express();
const port = 1245;
const database = process.argv[2];

async function requestListener(req, res) {
  res.setHeader('Content-Type', 'text/plain');

  switch (req.url) {
    case '/':
      res.writeHead(200);
      res.end('Hello Holberton School!');
      break;
    case '/students':
      res.writeHead(200);
      res.write('This is the list of our students\n'); // Add a newline for separation
      try {
        const data = await fs.readFile(database, 'utf8');
        const rows = data.trim().split('\n').slice(1); // Trim and split data

        const studentsCS = [];
        const studentsSWE = [];

        for (const row of rows) {
          // eslint-disable-next-line
          if (row.trim() === '') continue; // Skip empty lines

          const columns = row.split(',');

          if (columns[3] === 'CS') {
            studentsCS.push(columns[0]);
          }

          if (columns[3] === 'SWE') {
            studentsSWE.push(columns[0]);
          }
        }

        res.write(`Number of students: ${studentsCS.length + studentsSWE.length}\n`);
        res.write(`Number of students in CS: ${studentsCS.length}. List: ${studentsCS.join(', ')}\n`);
        res.write(`Number of students in SWE: ${studentsSWE.length}. List: ${studentsSWE.join(', ')}\n`);
        res.end(); // End the response
      } catch (err) {
        res.status(500).end('Cannot load the database');
      }
      break;
    default:
      res.writeHead(404);
      res.end('Not Found');
      break;
  }
}

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', requestListener);

app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});

module.exports = app;
