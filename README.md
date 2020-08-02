# Music-Streaming-Website
A Music Streaming, Sharing, and Management Platform. A user should be
able to upload/download/play/delete/search songs. All songs go into a common playlist
(which shows up when the user wants to view all songs).

## Technologies Used
  - **Backend**
    - Python
    - Flask Framework
    - Jinja Templates
    - SQLite3
  - **Frontend**
    - HTML
    - CSS
    - JavaScript
    - Bootstrap
  - **Database**
    - SQL
  - **For File Storage**
    - [Azrue Storage](https://docs.microsoft.com/en-us/azure/?product=featured)

## Functional Description

- Upload a song
  - Has metadata fields title, artist, album
  - Users can upload any song of his own choice. After successful upload of song, it will appear in the playlist section

- Delete an uploaded song
- View all songs/view playlist
- Search for any song via album/title/artist
- Stream song
  - Each song should have a page where you can play the song from the browser itself.
  - Clicking on the unique URL of a song should lead to this page.
  - Clicking on a song entity from either search or view all pages should also lead to this page.
  - There should be an option to download this song.
  - Users can also share this link with some other person so that other people will also come to the same song page if he/she hits the URL directly.

    
## Prerequisites
  - Python3 should be installed
## How to launch the Application
to run the application type `source run.sh`. 
- **Important**
   - `run.sh` is only compatible with Linux/Ubuntu/MacOs.
   - Running the script just using the `run.sh` the command will execute the script in a separate subshell.
   - `source run.sh` the command will run within the existing shell, ensuring any variables created or modified by the script will be available after the script
   completes.
   
## Setting up the Environment
Directly running the script will lead to an error because we have to set below the listed environment variables before actually launching the script. So, just substitute the following variables with their appropriate values.
  - `export STORAGE_ACCOUNT_CONNECTION_STRING="your_storage_account_connection_string"`
  - `export STORAGE_CONTAINER_NAME="your_storage_account_container_name"`
  - `export BLOB_URL="your_storage_account_container_url"`
  
## Home Page
[![Screenshot-2020-08-02-at-9-44-49-PM.png](https://i.postimg.cc/vTss1Qc0/Screenshot-2020-08-02-at-9-44-49-PM.png)](https://postimg.cc/ygv5tChR)

## Upload Page
[![Screenshot-2020-08-02-at-9-46-18-PM.png](https://i.postimg.cc/3xcQXjk4/Screenshot-2020-08-02-at-9-46-18-PM.png)](https://postimg.cc/68nPwvLt)

## Playlist Page / Stream Page
[![Screenshot-2020-08-02-at-9-48-21-PM.png](https://i.postimg.cc/t4PNkpT3/Screenshot-2020-08-02-at-9-48-21-PM.png)](https://postimg.cc/21kW8pny)

## Search Page
[![Screenshot-2020-08-02-at-9-49-51-PM.png](https://i.postimg.cc/L8zjfDCv/Screenshot-2020-08-02-at-9-49-51-PM.png)](https://postimg.cc/QFdBZQrW)

## Streaming a Song
[![Screenshot-2020-08-02-at-9-50-52-PM.png](https://i.postimg.cc/QC9TMJKQ/Screenshot-2020-08-02-at-9-50-52-PM.png)](https://postimg.cc/H8mxZ52n)
