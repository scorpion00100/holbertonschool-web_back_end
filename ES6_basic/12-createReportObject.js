export default function createReportObject(employeesList) {
    return {
      getNumberOfDepartments() {
        return Object.keys(employeesList).length;
      },
      allEmployees: employeesList,
    };
  }
  