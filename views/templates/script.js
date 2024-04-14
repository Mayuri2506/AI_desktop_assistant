function start() {
        eel.start()();

    }

    eel.expose(updateUserLog);
    eel.expose(updateSystemLog);

    function updateUserLog(message) {
        var userLogContainer = createMessageContainer('user-message', message);
        scrollToBottom();
    }

    function updateSystemLog(message) {
        var systemLogContainer = createMessageContainer('system-message', message);
        scrollToBottom();
        if (message.includes("Thanks for using me") || message.includes("Goodbye")) {
        // Show the horizontal line
        var hrElement = document.createElement('hr');
        hrElement.classList.add('break-line');
        document.getElementById("center-container").appendChild(hrElement);
    }
    }

    function createMessageContainer(className, message) {
        var container = document.getElementById('center-container');
        var messageContainer = document.createElement('div');
        messageContainer.className = 'message-container ' + className;
        messageContainer.innerHTML = message;
        container.appendChild(messageContainer);
    }
    eel.expose(getContact)
    function getContact() {
            var contact = prompt("Enter the contact number to send the message with the country code:");
            return contact;
        }
    eel.expose(getEmail)
    function getEmail() {
            var Email = prompt("Enter Recipient's Email ID");
            return Email;
        }
    eel.expose(getFilename)
    function getFilename() {
            var fname = prompt("Enter the file name with extension");
            return fname;
        }
    function scrollToBottom() {
        var container = document.getElementById('center-container');
        container.scrollTop = container.scrollHeight;
    }