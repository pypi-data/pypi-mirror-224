<p>edit the plan. ID = {{no}}</p>
<form action="/edit/{{no}}" method="get">
    <input type="text" name="task" value="{{old[0]}}" size="100" maxlength="100">
    <select name="status">
        <option value="open">not completed</option>
        <option>eventually completed</option>
    </select>
    <br>
    <input type="submit" name="save" value="submit">
</form>
