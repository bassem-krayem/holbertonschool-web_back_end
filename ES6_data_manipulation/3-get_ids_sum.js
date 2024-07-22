export default function getStudentIdsSum(students) {
  return students.reduce((total, studentIds) => total + studentIds.id, 0);
}
