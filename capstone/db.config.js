module.exports = {
  HOST: "34.101.173.241",
  USER: "root",
  PASSWORD: "123",
  DB: "capstone123",
  dialect: "mysql",
  pool: {
    max: 5,
    min: 0,
    acquire: 30000,
    idle: 10000
  }
};