# Parec Frontend

## UX Components

### Search bar

Search bar + button that takes arbitrary input from user and passes it on to the backend as use query.

### Graph

Graph representing the relationship between the terms found in the backend.

User query is central node, with each other node being child node to the node of the term that was searched to find the term of that node.

Graph is rebuilt after every query.
### Paper list

List of papers from the database related to the user query and found relevant terms, as returned from the backend.

Each paper is provided with its title, authors and link.

### API value field

Currently debugging field showing the vale returned from the API.

To be refactored into general status field.

## Design Decisions

ToDO

## Usage

```
npm run dev
npm run build
```
