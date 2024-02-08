#variables, tipos de datos

def reto3():          
        n=[];
        entrada= int(input("¿cuantos usuarios desea ingresar?-> "));
        for i in range(entrada):
                n.append(i+1);
                name = str(input("ingresa tu nombre(s)-> "));
                if len(name)<5 or len(name)>50:
                        print("la cantidad de caracteres no es valida");
                        print("da enter para continuar");
                        input();
                        return reto3();
                apellidos = str(input("ingresa tus apellidos-> "));
                if len(apellidos)<5 or len(apellidos)>50:
                        print("la cantidad de caracteres no es valida");
                        print("da enter para continuar");
                        input();
                        return reto3();
                numero = int(input("ingresa tu numero de telefono-> "));
                if numero<11:
                        print("la cantidad de caracteres no es valida");
                        print("da enter para continuar");
                        input();
                        return reto3();
                correo = str(input("ingresa tu correo->"));
                if len(correo)<5 or len(correo)>50:
                        print("la cantidad de caracteres no es valida");
                        print("da enter para continuar");
                        input();
                        return reto3();
                print("usuario registrado correctamente \n");
        print("lista de usuarios registrados: ",n);
reto3();


     
