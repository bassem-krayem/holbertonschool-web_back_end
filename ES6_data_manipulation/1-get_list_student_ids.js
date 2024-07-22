export default function getListStudentIds(array) {
  if (!Array.isArray(array)) {
    return [];
    // eslint-disable-next-line
  } else {
    return array.map((id) => id.id);
  }
}
