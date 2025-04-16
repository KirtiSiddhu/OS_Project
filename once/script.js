// function showForm(type) {
//   const container = document.getElementById("form-container");
//   let html = '';

//   switch (type) {
//     case 'add':
//       html = `
//         <h3>Add Entry</h3>
//         <input type="text" id="addPath" placeholder="Enter directory path">
//         <button onclick="addEntry()">Submit</button>`;
//       break;
//     case 'remove':
//       html = `
//         <h3>Remove Entry</h3>
//         <input type="text" id="removePath" placeholder="Enter entry to remove">
//         <button onclick="removeEntry()">Submit</button>`;
//       break;
//     case 'update':
//       html = `
//         <h3>Update Entry</h3>
//         <input type="text" id="oldEntry" placeholder="Old entry">
//         <input type="text" id="newEntry" placeholder="New entry">
//         <button onclick="updateEntry()">Submit</button>`;
//       break;
//     case 'createFile':
//       html = `
//         <h3>Create File</h3>
//         <input type="text" id="fileDir" placeholder="Directory path">
//         <input type="text" id="fileName" placeholder="File name (e.g., example.txt)">
//         <textarea id="fileContent" placeholder="File content (optional)"></textarea>
//         <button onclick="createFile()">Submit</button>`;
//       break;
//     case 'removeFile':
//       html = `
//         <h3>Remove File</h3>
//         <input type="text" id="removeFilePath" placeholder="Full file path">
//         <button onclick="removeFile()">Submit</button>`;
//       break;
//   }

//   container.innerHTML = html;
// }

// function addEntry() {
//   const path = document.getElementById("addPath").value;
//   displayOutput(`Adding entry: ${path}`);
// }

// function removeEntry() {
//   const path = document.getElementById("removePath").value;
//   displayOutput(`Removing entry: ${path}`);
// }

// function updateEntry() {
//   const oldEntry = document.getElementById("oldEntry").value;
//   const newEntry = document.getElementById("newEntry").value;
//   displayOutput(`Updating '${oldEntry}' to '${newEntry}'`);
// }

// function listEntries() {
//   // Example static entries
//   const entries = ['Documents/Work', 'Projects/AI', 'Downloads/Reports'];
//   displayOutput(`Directory Entries:\n${entries.map((e, i) => `${i + 1}. ${e}`).join('\n')}`);
// }

// function createFile() {
//   const dir = document.getElementById("fileDir").value;
//   const name = document.getElementById("fileName").value;
//   const content = document.getElementById("fileContent").value;
//   displayOutput(`Creating file: ${dir}/${name}\nWith content:\n${content}`);
// }

// function removeFile() {
//   const path = document.getElementById("removeFilePath").value;
//   displayOutput(`Removing file: ${path}`);
// }

// function exitSystem() {
//   if (confirm("Are you sure you want to exit the Directory Management System?")) {
//     window.close(); // May not work in browser, fallback below
//     document.querySelector(".container").innerHTML = `
//       <h1 style="text-align:center; color:#00ffcc;">System Closed</h1>
//       <p style="text-align:center;">You have exited the Directory Management System. Have a great day!</p>
//     `;
//   }
// }

// function displayOutput(message) {
//   document.getElementById("output").innerText = message;
// }


document.addEventListener("DOMContentLoaded", () => {
  const startVoiceButton = document.getElementById("start-voice");
  const outputDiv = document.getElementById("output");

  // Web Speech API for voice recognition
  const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  recognition.lang = "en-US";

  startVoiceButton.addEventListener("click", () => {
      recognition.start();
      outputDiv.textContent = "Listening...";
  });

  recognition.onresult = (event) => {
      const command = event.results[0][0].transcript;
      outputDiv.textContent = `You said: ${command}`;
      sendCommandToBackend(command);
  };

  recognition.onerror = (event) => {
      outputDiv.textContent = `Error: ${event.error}`;
  };

  function sendCommandToBackend(command) {
      fetch("/api/command", {
          method: "POST",
          headers: {
              "Content-Type": "application/json",
          },
          body: JSON.stringify({ command }),
      })
          .then((response) => response.json())
          .then((data) => {
              if (data.message) {
                  outputDiv.textContent = data.message;
              } else if (data.entries) {
                  outputDiv.textContent = `Entries: ${data.entries.join(", ")}`;
              } else if (data.error) {
                  outputDiv.textContent = `Error: ${data.error}`;
              }
          })
          .catch((error) => {
              outputDiv.textContent = `Error: ${error.message}`;
          });
  }
});