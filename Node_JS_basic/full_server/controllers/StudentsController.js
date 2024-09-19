const readDatabase = require("../utils");
// Get database filename
// const database = process.argv[2];

const database = process.argv[process.argv.length -1];

export default class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const students = await readDatabase(database);
      const { CS, SWE } = students;

      res.status(200);
      res.write('This is the list of our students\n');

      res.write(`Number of students in CS: ${CS.length}. List: ${CS.join(', ')}\n`);
      res.end(`Number of students in SWE: ${SWE.length}. List: ${SWE.join(', ')}`);
  } catch (err) {
    res.status(500);
    res.end('Cannot load the database');
  }
  }
  static async getAllStudentsbyMajor(req, res) {
    try {
      const students = await readDatabase(database);
      const { CS, SWE } = students; 

      if (req.params['major'] === 'CS') {
          res.status(200);
          res.send(`List: ${CS.join(', ')}`);
      } else if ((req.params['major'] === 'SWE')) {
          res.status(200);
          res.send(`List: ${SWE.join(', ')}`);
      } else {
        res.status(500);
        res.end('Major parameter must be CS or SWE');
      }
    } catch (err) {
      res.status(500);
      res.end('Cannot load the database');
    }
  }
}