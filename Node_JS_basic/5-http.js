const http = require('http');
const fs = require('fs').promises;
// eslint-disable-next-line
const path = require('path');

// Define the countStudents function
async function countStudents(filePath) {
  let output = '';
  try {
    const data = await fs.readFile(filePath, 'utf-8');
    if (data) {
      const rows = data.trim().split('\n');
      const totalStudents = rows.length - 1;
      output += `Number of students: ${totalStudents}\n`;

      const studentsByField = {};

      rows.slice(1).forEach((row) => {
        const columns = row.split(',');
        const firstName = columns[0];
        const field = columns[columns.length - 1];

        if (!studentsByField[field]) {
          studentsByField[field] = [];
        }
        studentsByField[field].push(firstName);
      });

      for (const field in studentsByField) {
        if (Object.hasOwnProperty.call(studentsByField, field)) {
          const students = studentsByField[field];
          output += `Number of students in ${field}: ${students.length}. List: ${students.join(', ')}\n`;
        }
      }
    }
  } catch (error) {
    output = 'Cannot load the database';
  }
  return output;
}

// Get the CSV file path from command line arguments
const csvFilePath = process.argv[2];

// Create an HTTP server
const app = http.createServer(async (req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.write('Hello Holberton School!');
    res.end();
  } else if (req.url.startsWith('/students')) {
    try {
      const output = await countStudents(csvFilePath); // Await the result of countStudents

      res.writeHead(200, { 'Content-Type': 'text/plain' });
      res.write('This is the list of our students\n');
      res.write(output); // Write the captured output
      res.end();
    } catch (error) {
      res.writeHead(500, { 'Content-Type': 'text/plain' });
      res.write('Internal Server Error');
      res.end();
    }
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.write('Not Found');
    res.end();
  }
});

// Server listens on port 3000
const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Server is listening on port ${PORT}`);
});


module.exports = app;
