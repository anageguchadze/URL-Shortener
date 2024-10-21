# Django URL Shortener

This project is a simple URL shortening web application built using Django. It allows users to input a long URL and receive a shortened URL in return. The shortened URL redirects users to the original long URL, and the system tracks the number of visits for each shortened URL.

## Features

- **Shorten URL**: Users can enter a long URL and get a unique short URL in return.
- **Redirect**: The short URL redirects to the original long URL.
- **Track Visits**: Keeps track of how many times the short URL has been accessed.
- **View Statistics**: Provides visit statistics for each shortened URL.

## Models

1. **URL**
   - `long_url`: The original long URL entered by the user.
   - `short_url`: A unique short string that maps to the long URL.
   - `visits`: A counter that tracks how many times the short URL has been visited.

## Installation and Setup

### Prerequisites

- Python 3.x
- Django 4.x
- A virtual environment (recommended)

### Steps to Run the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/anageguchadze/URL-Shortener
