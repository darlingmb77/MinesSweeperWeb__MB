# Minesweeper Strategy Game – Prototype

Author: Sherri Brice  
Date: 2026  

## Prototype Overview

This prototype demonstrates the early structure and functionality of a web-based Minesweeper strategy game application. The goal of the project is to create a browser-based game that allows users to play Minesweeper while tracking scores and gameplay statistics through a connected database.

The prototype focuses on demonstrating the core architecture of the application, including the front-end interface, backend server logic, and database interaction.

---

## Technologies Used

- Python
- Flask
- SQLite Database
- HTML5
- CSS
- JavaScript
- GitHub for version control

---

## Current Prototype Features

### Game Interface Layout

The prototype includes a basic user interface that reflects the planned layout of the final application.

Features include:

- Application banner labeled **Minesweeper**
- User input field for entering a player name
- Start Game button
- Placeholder Minesweeper game board
- Two leaderboard columns:
  - Top Scores
  - Longest Times

This layout was designed using HTML and CSS and is structured to support future interactive gameplay logic.

---

### Leaderboard System

The application includes a functioning backend API that retrieves leaderboard data from an SQLite database.

Flask API endpoint:




The leaderboard page dynamically loads and displays these records using JavaScript.

---

### Database Integration

The prototype uses SQLite to store player score data.

The database table stores:

- Player name
- Score
- Date

This demonstrates how game results can later be recorded and displayed.

---

### Instructional Video Integration

A YouTube tutorial video explaining how to play Minesweeper is embedded into the interface. This provides users with guidance before gameplay begins and demonstrates the ability to integrate external content into the application.

---

## Screenshots

(Add screenshots of:)

- Home page layout
- Game interface
- Leaderboard page
- Database results

These screenshots illustrate the visual structure and current functionality of the prototype.

---

## Planned Future Development

Future development will include:

- Full Minesweeper gameplay logic
- Timer tracking for longest game times
- Score submission when a game is completed
- Dynamic leaderboard updates
- Improved user interface styling
- Deployment of the application to a hosted web server

---

## Summary

This prototype demonstrates the foundational structure of the Minesweeper strategy game system. While the gameplay mechanics are still under development, the current prototype establishes the architecture necessary for database connectivity, user interaction, and front-end interface design.

The system provides a strong starting point for further development into a fully functional educational web application.