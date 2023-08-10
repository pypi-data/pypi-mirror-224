Code level software performance measuring. Measuring is done by defining action start and end point in code.

## Import
```
from Perfole.Perfole import PERFORMANCE_TEST
```

## Set start/end points
```
    PERFORMANCE_TEST.StartAction("actionName", ...)
    ...
    PERFORMANCE_TEST.EndAction("actionName", ...)
```


## Start/stop measurement
```
    PERFORMANCE_TEST.Start(True)
    ...
    PERFORMANCE_TEST.Stop()
```


## Expected methods order
```
PERFORMANCE_TEST.Start()  // before action points


PERFORMANCE_TEST.StartAction() // anywhere beetwen start/stop measurement
...
PERFORMANCE_TEST.EndAction() // anywhere beetwen start/stop measurement


PERFORMANCE_TEST.Stop() // after all action points
```

## Results
Stop() method will return list of caught actions. For cloud reporting functionality visit https://perfole.com


## Multithreaded code

In multithreaded code, when start and stop events are called in different threads, uniqueIdentifier parameter must be given. E.g:

```
PERFORMANCE_TEST.StartAction(name="actionName", uniqueIdentifier= "myIdentifier")
...
PERFORMANCE_TEST.EndAction(name="actionName", uniqueIdentifier= "myIdentifier")
```









