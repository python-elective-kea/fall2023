# Build in functions, top level syntax, datamodel methods

## this is an overview of how the build in functions are connected to its datamodel method. 
The build in function is caling the datamodel method. just like in othe languages.

<table>
  <thead>
    <tr>
      <th>Top-level syntaks</th>
      <th>Dundermetode</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>x + y</td>
      <td><code>__add__(self, other)</code></td>
    </tr>
    <tr>
      <td>x - y</td>
      <td><code>__sub__(self, other)</code></td>
    </tr>
    <tr>
      <td>x * y</td>
      <td><code>__mul__(self, other)</code></td>
    </tr>
    <tr>
      <td>x / y</td>
      <td><code>__truediv__(self, other)</code></td>
    </tr>
    <tr>
      <td>x // y</td>
      <td><code>__floordiv__(self, other)</code></td>
    </tr>
    <tr>
      <td>x % y</td>
      <td><code>__mod__(self, other)</code></td>
    </tr>
    <tr>
      <td>x ** y</td>
      <td><code>__pow__(self, other)</code></td>
    </tr>
    <tr>
      <td>x == y</td>
      <td><code>__eq__(self, other)</code></td>
    </tr>
    <tr>
      <td>x != y</td>
      <td><code>__ne__(self, other)</code></td>
    </tr>
    <tr>
      <td>x &gt; y</td>
      <td><code>__gt__(self, other)</code></td>
    </tr>
    <tr>
      <td>x &lt; y</td>
      <td><code>__lt__(self, other)</code></td>
    </tr>
    <tr>
      <td>x &gt;= y</td>
      <td><code>__ge__(self, other)</code></td>
    </tr>
    <tr>
      <td>x &lt;= y</td>
      <td><code>__le__(self, other)</code></td>
    </tr>
    <tr>
      <td>x(x1, x2, ..., xn)</td>
      <td><code>__call__(self, *args, **kwargs)</code></td>
    </tr>
    <tr>
      <td>len(x)</td>
      <td><code>__len__(self)</code></td>
    </tr>
    <tr>
      <td>str(x)</td>
      <td><code>__str__(self)</code></td>
    </tr>
    <tr>
      <td>repr(x)</td>
      <td><code>__repr__(self)</code></td>
    </tr>
    <tr>
      <td>x[index]</td>
      <td><code>__getitem__(self, index)</code></td>
    </tr>
    <tr>
      <td>x[index] = value</td>
      <td><code>__setitem__(self, index, value)</code></td>
    </tr>
    <tr>
      <td>del x[index]</td>
      <td><code>__delitem__(self, index)</code></td>
    </tr>
    <tr>
      <td>x in y</td>
      <td><code>__contains__(self, item)</code></td>
    </tr>
    <tr>
      <td>with x as y:</td>
      <td><code>__enter__(self)</code> and <code>__exit__(self, exc_type, exc_val, exc_tb)</code></td>
    </tr>
  </tbody>
</table>



