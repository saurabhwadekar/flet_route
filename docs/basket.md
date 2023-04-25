# Basket

## what is basket
`Basket` is one way. To share `data` or `objects` in multiple `views`. It is available as a `parameter` to every `view` and `middleware`. In this, you can perform operations like `get`, `add`, `update`, `delete` by the methods given below.

## Add variable to basket

```python
basket.my_data = {"name":"saurabh","mob":"1234567890","email":"example@gamil.com"}
```

## Get variable from basket
variable access from basket
```python
basket.my_data
```
Accessing a variable using the `get()` method.
In get method we have to give the `name` of the variable in the form of `string`.
If the variable exists then it will return the `value` otherwise it will return `None`.
```python
basket.get("my_data")
```

## Updating variable in basket
If a variable named `my_data` does not exist in `basket`, a new variable named `my_data` will be created.
```python
basket.my_data = [1,2,3,4,5,6,7,8]
```

## Delete variable from basket
deleting a variable using the `del` keyword
```python
del basket.my_data
```
deleting a variable using the `delete()` method.
In the `delete()` method, you have to pass the `name` of the variable as a `string`. It will not give an error if a variable with this name does not exist in `basket`.
```python
basket.delete("my_data")
```


