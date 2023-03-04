// Вид 1
void Method1()
{
    System.Console.WriteLine("Автор ...");
}
//Method1();

//Вид 2. Методы, которые принимают аргументы, но не возвращают их
void Method2(string msg)
{
    System.Console.WriteLine(msg);
}
//Method2("Текст сообщения");

void Method21(string msg, int count)
{
    int i = 0;
    while (i < count)
    {
        System.Console.WriteLine(msg);
        i++;
    }
}
//Method21(msg: "Sueta", count: 4);



//Вид 3. Методы, которые что-то возвращают, но ничего не принимают

int Method3()
{
    return DateTime.Now.Year;
}

int year = Method3();
//System.Console.WriteLine(year);






//Вид 4. Методы которые что-то принимают и что-то возвращают
string Method4(int count, string text)
{
    int i = 0;
    string result = String.Empty;
    while (i < count)
    {
        result = result + text;
        i++;
    }
    return result;
}

string res = Method4(10, "Я уеду в Комарово ");
System.Console.WriteLine(res);

