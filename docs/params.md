# Params
## what is params
`params` we get as parameter in view.
which is an object of `Params` class
In which we get all the `values` ​​extracted from `url` in the form of `variables`. These variables can also be `get`,`add`, `delete`, `update` in the following ways.
This would be useful in middlewares in general.

## Add variable to params

```python
params.stu_id = 11
```

## Get variable from params
variable access from `params`
```python
params.stu_id
```
Accessing a variable using the `get()` method.
In get method we have to give the `name` of the variable in the form of `string`.
If the variable exists then it will return the `value` otherwise it will return `None`.
```python
params.get("stu_id")
```

## Updating variable in params
If a variable named `stu_id` does not exist in `params`, a new variable named `stu_id` will be created.
```python
params.stu_id = 22
```

## Delete variable from params
deleting a variable using the `del` keyword
```python
del params.stu_id
```
deleting a variable using the `delete()` method.
In the `delete()` method, you have to pass the `name` of the variable as a `string`. It will not give an error if a variable with this name does not exist in `params`.
```python
params.delete("stu_id")
```


