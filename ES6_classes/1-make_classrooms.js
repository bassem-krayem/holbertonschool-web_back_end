import ClassRoom from './0-classroom.js';

export default function initializeRooms() {
  const myRoom1 = new ClassRoom(19);
  const myRoom2 = new ClassRoom(20);
  const myRoom3 = new ClassRoom(34);
  return [myRoom1, myRoom2, myRoom3];
}
