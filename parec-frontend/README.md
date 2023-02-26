***
ℹ️ This directory contains the frontend code for the Parec application, which provides a web interface for users to interact with the Parec backend. It includes the following subdirectories and files:
***

- **🗂️ [`public/`](parec-frontend/public):** Contains ...

- **🗂️ [`src/`](parec-frontend/src):** This directory contains the source code for the frontend application:

    - **🌐 [`App.svelte`](parec-frontend/App.svelte):** The file is the main component of the Parec frontend web application, which contains the routing logic and renders other components.

    - **🌐 [`main.js`](parec-frontend/main.js):** This file is the entry point for the Parec frontend web application, which initializes the root component and attaches it to the DOM.

    - **🌐 [`vite-env.d.ts`](parec-frontend/vite-env.d.ts):** It contains the type declarations for environment variables used by [Vite](https://vitejs.dev), the build tool used to build the Parec frontend application.

- **🛳️ [`Dockerfile`](parec-frontend/Dockerfile):** This Dockerfile builds and deploys a frontend application using `Node.js` and `Nginx`, copying over the necessary files and configurations and installing required dependencies in the process.








