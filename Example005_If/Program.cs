Console.Write("Введите имя пользователя: ");
string username = Console.ReadLine();

if (username.ToLower() == "Маша")
{
    Console.WriteLine("Ура! Это же Ее величетсво МАРИЯ!");
}
else
{
    Console.Write("Приветствую, ");
    Console.WriteLine(username);
}