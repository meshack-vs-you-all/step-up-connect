FROM klakegg/hugo:ext-alpine

WORKDIR /src

COPY . .

# Expose port
EXPOSE 1313

# Command to run the application
CMD ["server", "-D", "--bind", "0.0.0.0"]
