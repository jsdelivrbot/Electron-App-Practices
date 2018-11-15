const electron = require('electron')
const ffmpeg = require('fluent-ffmpeg')

const {app, BrowserWindow , ipcMain} = electron;
let mainWindow;

app.on('ready', ()=>{
   // console.log('App is now ready');
   mainWindow = new BrowserWindow({});
   mainWindow.loadURL(`file://${__dirname}/views/index.html`);
});

ipcMain.on("getVideoFileLength",(event,path)=>{
    ffmpeg.ffprobe(path,(err,metadata)=>{
        console.log('Video duration is:' ,metadata.format.duration);
        mainWindow.webContents.send('videoRenderedDuration', metadata.format.duration);
    });
});

