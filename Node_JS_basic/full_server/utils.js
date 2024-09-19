const fs = require('fs').promises;

module.exports = async function readDatabase(path) {
  try {
    const data = await fs.readFile(path, 'utf-8');
    const rows = data.split('\n').slice(1);

    const studentsCS = [];
    const studentsSWE = [];

    for (const row of rows) {
      const data = row.split(',');

      // if field is CS add to CS array
      if (data[3] === 'CS') {
        studentsCS.push(data[0]);
      }
      // if field is SWE add to SWE array
      if (data[3] === 'SWE') {
        studentsSWE.push(data[0]);
      }
    }

    return {
      CS: studentsCS,
      SWE: studentsSWE,
    };
  } catch (err) {
    throw new Error('Cannot load the database');
  }
};
