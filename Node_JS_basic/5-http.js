const http = require('http');
const fs = require('fs').promises;

const host = 'localhost';
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
        const rows = data.split('\n').slice(1);

        const studentsCS = [];
        const studentsSWE = [];

        for (const row of rows) {
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
        res.end('Cannot load the database');
      }
      break;
    default:
      res.writeHead(404);
      res.end('Not Found');
      break;
  }
}

const app = http.createServer(requestListener);
app.listen(port, host, () => {
  console.log(`Server running at http://${host}:${port}/`);
});

module.exports = requestListener;
