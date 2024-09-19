const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');

    if (data) {
      const rows = data.trim().split('\n');
      const totalStudents = rows.length - 1;

      console.log(`Number of students: ${totalStudents}`);

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
          console.log(`Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`);
        }
      }
    }
  } catch (er) {
    throw new Error('Cannot load the database');
    // eslint-disable-next-line
    console.error(er);
  }
}

module.exports = countStudents;
