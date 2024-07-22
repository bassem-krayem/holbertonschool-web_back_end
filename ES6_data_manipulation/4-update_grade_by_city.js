export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.location === city) // Step 1: Filter students by city
    .map((student) => {
      // Step 2: Find the grade for this student or default to 'N/A'
      const gradeEntry = newGrades.find(
        // eslint-disable-next-line
        (entry) => entry.studentId === student.id
      );
      const grade = gradeEntry ? gradeEntry.grade : 'N/A';

      // Return a new object with updated grade
      return { ...student, grade };
    });
}
