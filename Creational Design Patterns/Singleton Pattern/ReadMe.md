# Singleton Patterns

Ensures that a class has only one isntance and provides a global point of access to that instance.
1. Private Constructor: Prevents instantiation from outside the class.
2. Static Variable: Holds the single instance of the class
3. Public Static Method: Provide a global access point to get the instance.

## Eager Singleton
### Pros
Thread Safe

### Cons
Wastes memory if the instance is never used.
Not suitable for heavy objects.

## Lazy Loading

### Pros
Saves memory
Object creation is deferred untill required.

### Cons
Not Thread Safe

## Bill Pugh Singleton
