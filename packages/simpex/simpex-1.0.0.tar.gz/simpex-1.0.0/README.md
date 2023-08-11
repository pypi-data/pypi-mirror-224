# Simpex

> 'simpex' stands for 'simple regex'

- Simplifies the process of using regex in python

<br>

## Usage:

> Installation: `pip install simpex`

#### Custom:

- Given a sample data set with minimum 2 values, it will return a regex pattern
- Example:

```
import simpex

data_set = ['example@gmail.com',
            'test@yahoo.com',
            'admin@proton.me']

pattern = simpex(data_set)
```

#### Built-in:

- Use built-in methods to get regex pattern
- Check all available built-in methods in [wiki]()
- temp wiki:

```
patterns(pattern_name)
- pattern_name: str
- returns: regex pattern
- avaliable: `email`, `phone`, `url`, `ipv4`, `ipv6`, `mac`, `credit_card`, `date`, `hex_color`, `html_tag`
```

- Example:

```
import simpex

pattern = simpex.patterns('email')
```

<br>

> Custom / Built-in method will return the following pattern: `^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]*`

```
<br>
```

### API used

> all require string type data

| sr. | API url                                    | required data type          | outputs         |
| --- | ------------------------------------------ | --------------------------- | --------------- |
| 0   | information (this only)                    | none / null                 | this info - str |
| 1   | https://saasbase.dev/tools/regex-generator | english to regex (ai) - str | single - str   |
| 2   | https://www.autoregex.xyz                  | english to regex (ai) - str | single - str    |
| 3   | https://regex.murfasa.com                  | english to regex (ai) - str | single - str    |
| 4   | https://regex.ai                           | multiple data set           | multiple - list |
