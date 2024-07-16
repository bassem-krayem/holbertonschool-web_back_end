export default function createReportObject(employeesList) {
  return {
    allEmployees: {
      ...employeesList, // Spread the departments and employees into allEmployees
    },
    getNumberOfDepartments() {
      return Object.keys(this.allEmployees).length;
    },
  };
}
