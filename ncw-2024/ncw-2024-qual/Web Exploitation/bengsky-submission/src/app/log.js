const fs = require('fs');
const path = require('path');

const logFilePath = path.join(__dirname, 'userChanges.log');


const writeLogMessage = (logMessage) => {
    fs.appendFileSync(logFilePath, logMessage + '\n', 'utf-8');
};

process.on('message', (userData) => {
    writeLogMessage(`[+] ${new Date().toISOString()}: Modify user data: ${JSON.stringify(userData, null, 2)}`);
    process.send('Log entry added successfully!');
});
