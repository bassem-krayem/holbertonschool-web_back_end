export default function getStudentsByLocation(students, city) {
  // eslint-disable-next-line
  return students.filter((student_city) => student_city.location === city);
}
