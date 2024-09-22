import express from 'express';
import AppController from '../controllers/AppController';
import StudentsController from '../controllers/StudentsController';

const router = express.Router();

// route '/'
router.get('/', AppController.getHomepage);

// route '/students'
router.get('/students', StudentsController.getAllStudents);

// route '/students/:major' (corrected)
router.get('/students/:major', StudentsController.getAllStudentsByMajor);

module.exports = router;