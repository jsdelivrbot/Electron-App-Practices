const electron = require("electron")

const {
    app,
    BrowserWindow,
    ipcMain,
    Menu
} = electron;

let mainWindow;
let secondWindow;

app.on('ready', () => {
    mainWindow = new BrowserWindow({});
    mainWindow.loadURL(`file://${__dirname}/views/index.html`);
    mainWindow.on('closed', ()=>{app.quit()});
    const mainMenu = Menu.buildFromTemplate(menuTemplate);
    Menu.setApplicationMenu(mainMenu);
});

function invokeTodo(){
    secondWindow = new BrowserWindow({
        width: 300,
        height: 200,
        title: "Add New Todo"
    });
    secondWindow.loadURL(`file://${__dirname}/views/addTodo.html`);
    secondWindow.on('closed',()=> secondWindow = null);
}

ipcMain.on('todoItem',(event , item)=>{
    secondWindow.close();
    mainWindow.webContents.send('todoItemAdd',item);
});

const menuTemplate = [
    {
    label: 'file',
    submenu: [
    {
        label: 'New Todo',
        accelerator: process.platform === 'darwin' ? 'Command+N' : 'Ctrl+N',
        click(){
            invokeTodo();
        }
    },
    {
        label: 'Clear Todo',
        accelerator: process.platform === 'darwin' ? 'Command+c' : 'Ctrl+c',
        click(){
            mainWindow.webContents.send('clearTodo');
        }
    },
    {
        label: 'Quit',
        accelerator: process.platform === 'darwin' ? 'Command+Q' : 'Ctrl+Q',
        click(){
            app.quit();
        }
    }
    ]
}];
if (process.platform == 'darwin'){
    menuTemplate.unshift({});
}
if( process.env.NODE_ENV !== 'production'){
    menuTemplate.push({
        label: 'view',
        submenu:[
            {
                role:'reload'
            },
            {
            label: "toggle Developer Tools",
            accelerator: process.platform === 'darwin' ? 'Command+alt+i' : 'Ctrl++shift+i',
            click(item, focusedWindow){
                focusedWindow.toggleDevTools();
            }
        }]
    })
}