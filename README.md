# Checkmate

Online phishing attacks pose a complex problem to all online users. The Checkmate API provides a simple solution.

## Overview

 - Clients register themselves via the `/add` route and receive an API key.
 - Clients can then register user emails with the API using their key and the users' emails via the `/register`.
 - Registering a user provides them with three words and a four digit PIN.
 - The three words are generated using natural language processing to improve memorability.
 - Clients can retrive these credentials using their key and a user's email via the `/retrieve` route.
 - Clients can include these credentials in any correspondence with a user to provide mutual authentication.
 - This provides protection against online phishing attacks, since it is easy for a user to notice when the set of credentials is missing or incorrect (even if it is difficult for them to recall their own credentials for a specific client).
 - Sensitive information, such as API keys and user emails, are stored as PBKDF2 hashes with client-specific salts. 
 - Data is stored encrypted on a locally hosted MongoDB server.

## Release

Checkmate is a personal project and is only a proof of concept. As such, its development is ongoing.

## Roadmap

Possible future functionality:

 - Automated mutual authentication via an email client plugin
 - User consent confirmation before registration to the system (spam protection)
 - Unique authentication token system from API to client

## Authors

Developed by [Alistair Robinson](https://github.com/AlistairRobinson)

## Acknowledgements

- Dr Adam Chester (University of Warwick, Department of Computer Science) for providing insight into future development of the project