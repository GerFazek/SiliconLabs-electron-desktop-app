const { app, BrowserWindow } = require("electron");

let mainWindow;

app.on("ready", () => {
  mainWindow = new BrowserWindow({ width: 1200, height: 780 });
  mainWindow.loadFile("index.html");
});
