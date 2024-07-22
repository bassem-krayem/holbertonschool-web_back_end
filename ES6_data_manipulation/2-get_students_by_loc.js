export default function getStudentsByLocation(students, city) {
  return students.filter(
    (student_location) => student_location.location === city
  );
}
