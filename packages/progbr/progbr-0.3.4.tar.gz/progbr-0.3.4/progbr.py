def printar(printa):
    print(printa)


def wifi_see_s():
    try:
        import platform, os
        if platform.system() == "Windows":
            return os.system('netsh wlan show profiles')
        elif platform.system() == "Linux" or platform.system() == "Darwin":
            return os.system('sudo ls /etc/NetworkManager/system-connections')
        else:
            return "This code is intended for Windows, Linux, and macOS only."
    except Exception as e:
        return str(e)



def wifi_config(wifi_name):
    try:
        import platform, os, subprocess
        if platform.system() == "Windows":
            return os.system(f'netsh wlan show profile "{wifi_name}" key=clear')
        elif platform.system() == "Linux" or platform.system() == "Darwin":
            if platform.system() == "Darwin":
                output = subprocess.check_output(['security', 'find-generic-password', '-l', wifi_name, '-D', 'AirPort network password', '-w'], universal_newlines=True)
            else:
                output = subprocess.check_output(['nmcli', 'connection', 'show', wifi_name], universal_newlines=True)
            return output
        else:
            return "This code is intended for Windows, Linux, and macOS only."
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"


def wifi_senha_sal(wifi_name):
    try:
        import platform, subprocess
        if platform.system() == "Windows":
            info = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi_name, 'key' ,'=', 'clear'])
            for linha in info.split('\n'):
                if "Conteúdo da chave" in linha:
                    pos = linha.find(':')
                    senha = linha[pos:]
                    return senha
        elif platform.system() == "Linux" or platform.system() == "Darwin":
            if platform.system() == "Darwin":
                output = subprocess.check_output(['security', 'find-generic-password', '-l', wifi_name, '-D', 'AirPort network password', '-w'], universal_newlines=True)
            else:
                output = subprocess.check_output(['nmcli', '-g', '802-11-wireless-security.psk', 'connection', 'show', wifi_name], universal_newlines=True)
            return output.strip()
        else:
            return "This code is intended for Windows, Linux, and macOS only."
    except Exception as e: return e


# Função para calcular o math.factorial de um número inteiro
def fatorial(n):
    try:
        import math
        return math.factorial(n)
    except Exception as e:
        return e

def eh_infinito(numero):
    try:
        import cmath
        if cmath.isfinite(numero):
            return f"{numero} É infinito"
        else:
            return f"{numero} É finito"
    except Exception as e: return e



def distancia_euclidiana(p, q) -> list:
    try:
        import math
        return math.dist(p, q)
    except Exception as e: return e

    
def raiz_cubico(numero:float):
    try:
        import sys, math

        if sys.version_info >= (3, 11):
            return math.cbrt(numero)
            # Código que utiliza recursos específicos do Python 3.11
            
        else:
            return numero * (1/3)
            # Código alternativo ou tratamento para versões mais antigas
    except Exception as e: raise e



# Função para calcular a potência de um número inteiro
def potencia(base, exponent):
    try:
        return base ** exponent
    except Exception as e:
        return e

# Função para calcular o máximo entre dois números inteiros
def valor_maximo(*args):
    try:
        return max(args)
    except Exception as e:
        return e
      
# Função para calcular o mínimo entre dois números inteiros
def valor_minimo(*args):
    try:
        return min(args)
    except Exception as e:
        return e

# Função para calcular a raiz quadrada de um número
def raiz_quadrada(num):
    try:
        import math
        return math.sqrt(num)
    except Exception as e:
        return e
    
def f_exponencial(x):
    import math
    return math.exp(-x)


def somar(*args):
    try:
        return sum(args)
    except Exception as e:
        return e

def comprimento_de(*args):
    try:
        return len(args)
    except Exception as e:
        return e
    
def em_ordem(*args):
    try:
        return sorted(args)
    except Exception as e:
        return e

def limpa():
    import os
    import platform
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def vetor(*args: list):
    try:
        import numpy as np
        return np.array(args)
    except Exception as e:
        return e
    

# Função para calcular o logaritmo natural de um número
def logaritmo_natural(num):
    try:
        import math
        return math.log(num)
    except Exception as e:
        return e

# Função para calcular o logaritmo na base 10 de um número
def logaritmo_base10(num):
    try:
        import math
        return math.log10(num)
    except Exception as e:
        return e

# Função para calcular a exponencial de um número
def exponencial(num):
    try:
        import math
        return math.exp(num)
    except Exception as e:
        return e
    
def PI():
    try:
        pi_value = 3.14159265358979323846
        return pi_value
    except Exception as e:
        return e

def PI_Long():
    try:
        pi_value =3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
        return pi_value
    except Exception as e: return e

def E_long():
    try:
        euler_value = 2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274
        return euler_value
    except Exception as e:
        return e

def E():
    try:
        # Obtém o valor de e com 200 casas decimais
        euler_value = 2.71828182845904523536

        return euler_value
    except Exception as e: return e


def Num_Au_long():
    try:
        import math as mp
        phi = (1 + mp.sqrt(5)) / 2
        return phi
    except Exception as e: return e

def Num_Au():
    try:
        import math as mp
        phi = (1 + mp.sqrt(5)) / 2
        return phi
    except Exception as e: return e


def Num_catalan(n):
    try:
        import math 
        numero = math.factorial(2*n) // (math.factorial(n+1) * math.factorial(n))
        return numero
    except Exception as e: return e


def feigenbaum_delta_long():
    try:
        feigenbaum_delta = 4.669201609102990671853203821578
        return feigenbaum_delta
    except Exception as e: return e

def feigenbaum_delta():
    try:
        from mpmath import mp
        mp.dps = 20
        feigenbaum_delta = 4.669201609102990671853203821578
        return feigenbaum_delta
    except Exception as e: return e


def feigenbaum_alfa():
   try:
        from mpmath import mp
        mp.dps = 20
        feigenbaum_alfa = 2.502907875095892822283902873218
        return feigenbaum_alfa
   except Exception as e: return e


def feigenbaum_alfa_long():
   try:
        from mpmath import mp
        mp.dps = 200
        feigenbaum_alfa = 2.502907875095892822283902873218
        return feigenbaum_alfa
   except Exception as e: return e


def Constante_de_Brun():
    from mpmath import mp
    mp.dps = 200
    brun = 1.9021605823
    return brun

# Função para calcular o logaritmo natural de um número + 1
def logaritmo_natural_mais_1(num):
    try:
        import math
        return math.log1p(num)
    except Exception as e:
        return e

# Função para calcular o valor absoluto de um número
def modulo(num):
    try:
        return abs(num)
    except Exception as e:
        return e

# Função para calcular o logaritmo na base 2 de um número
def logaritmo_base2(num):
    try:
        import math
        return math.log2(num)
    except Exception as e:
        return e

# Função para calcular o piso de um número
def piso(num):
    try:
        import math
        return math.floor(num)
    except Exception as e:
        return e

# Função para calcular o arredondamento de um número para o inteiro mais próximo
def arredondamento(num):
    try:
        return round(num)
    except Exception as e:
        return e

# Função para calcular o teto de um número
def teto_do_numero(num):
    try:
        import math
        return math.ceil(num)
    except Exception as e:
        return e
    
    

class Espera:
    def espera_s(n):
        import time
        time.sleep(n)

    def espera_m(n):
        import time
        time.sleep(n*60)

    def espera_h(n):
        import time
        time.sleep(n*3600)

    def espera_d(n):
        import time
        time.sleep(n*86400)
    
    def espera_me28(n):
        import time
        time.sleep(n*2419200)
    
    def espera_me29(n):
        import time
        time.sleep(n*2505600)
    
    def espera_me30(n):
        import time
        time.sleep(n*2592000)
    
    def espera_me31(n):
        import time
        time.sleep(n*2678400)
    
    def espera_tr30(n):
        import time
        time.sleep(n*7776000)

    def espera_tr31(n):
        import time
        time.sleep(n*2678400*3)

    def espera_sem(n):
        import time
        time.sleep(n * 604800)
    
    def espera_ano365(n):
        import time
        time.sleep(n*31536000)
    
    def espera_ano366(n):
        import time
        time.sleep(n*31622400)
    
    def espera_dec365(n):
        import time
        time.sleep(n*31536000*10)
    
    def espera_dec366(n):
        import time
        time.sleep(n*31622400*10)
    
    def miliseg(n):
        import time
        time.sleep(n / 1000)

    def esperar_e_desligar_m(n:int):
        try:
            import os
            n = n * 60
            os.system(f'shutdown /s /t {n}')
        except Exception as e:
            return e 
        
    def esperar_e_desligar_m(n: int):
        try:
            import subprocess
            if n <= 0:
                raise ValueError("O tempo deve ser maior que zero.")
            
            # Converte o tempo em minutos para segundos
            tempo_em_segundos = n * 60
            
            if subprocess.run(['sudo', 'shutdown', '-h', f'+{tempo_em_segundos}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0:
                print(f'Desligamento agendado em {n} minutos.')
            else:
                print('Falha ao agendar o desligamento.')
                
        except Exception as e:
            print(f'Erro: {e}') 
        
    def esperar_e_desligar(n: int):
        try:
            import subprocess, platform
            if n <= 0:
                raise ValueError("O tempo deve ser maior que zero.")
            
            # Converte o tempo em minutos para segundos
            tempo_em_segundos = n * 60
            
            # Verifica o sistema operacional
            sistema_operacional = platform.system()
            
            if sistema_operacional == 'Windows':
                comando_desligar = f'shutdown /s /t {tempo_em_segundos}'
            elif sistema_operacional in ('Linux', 'Darwin'):  # 'Darwin' é o nome do sistema operacional do macOS
                comando_desligar = f'shutdown -h +{tempo_em_segundos}'
            else:
                raise OSError("Sistema operacional não suportado.")
            
            # Executa o comando para desligar o computador
            resultado = subprocess.run(comando_desligar, shell=True)
            
            if resultado.returncode == 0:
                print(f'Desligamento agendado em {n} minutos.')
            else:
                print('Falha ao agendar o desligamento.')
            
        except Exception as e:
            return e
    
    def esperar_e_desligar_s(n: int):
        try:
            import subprocess, platform
            if n <= 0:
                raise ValueError("O tempo deve ser maior que zero.")
        
            
            # Verifica o sistema operacional
            sistema_operacional = platform.system()
            
            if sistema_operacional == 'Windows':
                comando_desligar = f'shutdown /s /t {n}'
            elif sistema_operacional in ('Linux', 'Darwin'):  # 'Darwin' é o nome do sistema operacional do macOS
                comando_desligar = f'shutdown -h +{n}'
            else:
                raise OSError("Sistema operacional não suportado.")
            
            # Executa o comando para desligar o computador
            resultado = subprocess.run(comando_desligar, shell=True)
            
            if resultado.returncode == 0:
                print(f'Desligamento agendado em {n} minutos.')
            else:
                print('Falha ao agendar o desligamento.')
                
        except Exception as e:
            return e
    
    def cancelar_desligamento():
        try:
            import platform, subprocess
            sistema_operacional = platform.system()
            
            if sistema_operacional == 'Windows':
                comando_cancelar_desligamento = 'shutdown /a'
            elif sistema_operacional in ('Linux', 'Darwin'):  # 'Darwin' é o nome do sistema operacional do macOS
                comando_cancelar_desligamento = 'sudo shutdown -c'
            else:
                raise OSError("Sistema operacional não suportado.")
            
            resultado = subprocess.run(comando_cancelar_desligamento, shell=True)
            
            if resultado.returncode == 0:
                print('Desligamento cancelado com sucesso.')
            else:
                print('Falha ao cancelar o desligamento.')
                
        except Exception as e:
            return e
        
    def suspender_computador():
        import os, platform
        system = platform.system()

        if system == 'Windows':
            os.system("shutdown /h")
        elif system == 'Darwin' or system == 'Linux':
            os.system("systemctl suspend")
        else:
            print("Suspensão não suportada neste sistema operacional.")
    



class Aleator:

    def alea_inteiro_a_b(a:int, b:int):
        try:
            import random
            if b < a:
                return "\033[4;7;31mO 'b' nao pode ser maior que 'a'"
            else:
                return random.randint(a, b)
        except Exception as e:
            return e
        
    def alea_inteiro_a(a:int):
        try:
            import numpy as radom
            return radom.random.randint(a)
        except Exception as e:
            return e
        
    def alea():
        import numpy as radom
        return radom.random.rand()

    def alea_num():
        import numpy as radom
        return radom.random.randn()
    
    
    def escolhe(escolha):
        try:
            from random import choice
            return choice(escolha)
        except Exception as e:
            return e
        
        
    

class Grafico:

    def grafico_barra(x=None, y=None, eixox=None, eixoy=None, titulo=None, cor=None, legenda=None, tamanho_d_figura=(8, 6), salvar_como=None, xlimite=None, ylimite=None):
        try:
            import matplotlib.pyplot as plt
            plt.rcParams['toolbar'] = 'None'
            if x is not None and y is not None:
                plt.figure(figsize=tamanho_d_figura)
                bars = plt.bar(x, y, color=cor)

                if eixox:
                    plt.xlabel(eixox)
                if eixoy:
                    plt.ylabel(eixoy)
                if titulo:
                    plt.title(titulo)
                if legenda:
                    plt.legend(bars, legenda)

                if xlimite:
                    plt.xlim(xlimite)
                if ylimite:
                    plt.ylim(ylimite)

                if salvar_como:
                    plt.savefig(salvar_como)
                else:
                    plt.show()

            else:
                # Aqui você pode adicionar alguma lógica para lidar com o caso em que x e y não são fornecidos.
                # Por exemplo, levantar um erro ou exibir uma mensagem informativa.
                pass

        except Exception as e:
            return e
    
    def grafico_dispersao(x=None, y=None, eixox=None, eixoy=None, titulo=None, cor=None, marcador='o', tamanho_d_figura=(8, 6), salvar_como=None, xlimite=None, ylimite=None):
        try:
            import matplotlib.pyplot as plt
            plt.rcParams['toolbar'] = 'None'
            if x is not None and y is not None:
                plt.figure(figsize=tamanho_d_figura)
                plt.scatter(x, y, color=cor, marker=marcador)

                if eixox:
                    plt.xlabel(eixox)
                if eixoy:
                    plt.ylabel(eixoy)
                if titulo:
                    plt.title(titulo)

                if xlimite:
                    plt.xlim(xlimite)
                if ylimite:
                    plt.ylim(ylimite)

                if salvar_como:
                    plt.savefig(salvar_como)
                else:
                    plt.show()

            else:
                # Aqui você pode adicionar alguma lógica para lidar com o caso em que x e y não são fornecidos.
                # Por exemplo, levantar um erro ou exibir uma mensagem informativa.
                pass

        except Exception as e:
            return e
    
    def grafico_pizza(dados=None, tamanhos=None, titulo=None, cor=None, destaca=None, tamanho_d_figura=(8, 6), salvar_como=None):
        try:
            import matplotlib.pyplot as plt
            plt.rcParams['toolbar'] = 'None'
            if dados is not None and tamanhos is not None:
                plt.figure(figsize=tamanho_d_figura)
                plt.pie(tamanhos, labels=dados, colors=cor, explode=destaca, autopct='%1.1f%%', shadow=True)

                if titulo:
                    plt.title(titulo)

                if salvar_como:
                    plt.savefig(salvar_como)
                else:
                    plt.show()

            else:
                # Aqui você pode adicionar alguma lógica para lidar com o caso em que labels e sizes não são fornecidos.
                # Por exemplo, levantar um erro ou exibir uma mensagem informativa.
                pass

        except Exception as e:
            return e
    
    def grafico_linhas(x, y, titulo=None, eixox=None, eixoy=None, tamanho_d_figura=(8, 6), salvar_como=None):
        try:
            import matplotlib.pyplot as plt
            plt.rcParams['toolbar'] = 'None'
            plt.figure(figsize=tamanho_d_figura)
            plt.plot(x, y)

            if titulo:
                plt.title(titulo)

            if eixox:
                plt.xlabel(eixox)

            if eixoy:
                plt.ylabel(eixoy)

            if salvar_como:
                plt.savefig(salvar_como)
            else:
                plt.show()

        except Exception as e:
            return e
    
    def grafico_area(x, y, titulo=None, eixox=None, eixoy=None, tamanho_d_figura=(8, 6), salvar_como=None):
        try:
            import matplotlib.pyplot as plt
            plt.rcParams['toolbar'] = 'None'
            plt.figure(figsize=tamanho_d_figura)
            plt.fill_between(x, y)

            if titulo:
                plt.title(titulo)

            if eixox:
                plt.xlabel(eixox)

            if eixoy:
                plt.ylabel(eixoy)

            if salvar_como:
                plt.savefig(salvar_como)
            else:
                plt.show()

        except Exception as e:
            return e
        
    

    def grafico_histograma(valores, titulo=None, eixox=None, eixoy=None, tamanho_d_figura=(8, 6), salvar_como=None):
        try:
            import matplotlib.pyplot as plt
            plt.rcParams['toolbar'] = 'None'
            plt.figure(figsize=tamanho_d_figura)
            plt.hist(valores, bins='auto', alpha=0.7, color='blue', edgecolor='black')

            if titulo:
                plt.title(titulo)

            if eixox:
                plt.xlabel(eixox)

            if eixoy:
                plt.ylabel(eixoy)

            if salvar_como:
                plt.savefig(salvar_como)
            else:
                plt.show()

        except Exception as e:
            return e
    
    

    def grafico_boxplot_(dados, titulo=None, eixox=None, tamanho_d_figura=(8, 6), salvar_como=None):
        try:
            import matplotlib.pyplot as plt
            plt.rcParams['toolbar'] = 'None'
            plt.figure(figsize=tamanho_d_figura)
            plt.boxplot(dados)

            if titulo:
                plt.title(titulo)

            if eixox:
                plt.xlabel(eixox)

            if salvar_como:
                plt.savefig(salvar_como)
            else:
                plt.show()

        except Exception as e:
            return e
    
    

    def grafico_boxplot(dados, titulo=None, eixox=None, tamanho_d_figura=(8, 6), salvar_como=None):
        try:
            import matplotlib.pyplot as plt
            plt.rcParams['toolbar'] = 'None'
            plt.figure(figsize=tamanho_d_figura)
            plt.boxplot(dados)

            if titulo:
                plt.title(titulo)

            if eixox:
                plt.xlabel(eixox)

            if salvar_como:
                plt.savefig(salvar_como)
            else:
                plt.show()

        except Exception as e:
            return e

        
        

    def surface_plot(x, y, z, titulo=None, eixox=None, eixoy=None, eixoz=None, tamanho_d_figura=(10, 8), salvar_como=None):
        try:
            import matplotlib.pyplot as plt
            plt.rcParams['toolbar'] = 'None'
            import numpy as np
            fig = plt.figure(figsize=tamanho_d_figura)
            ax = fig.add_subplot(111, projection='3d')
            ax.plot_surface(x, y, z, cmap='viridis')

            if titulo:
                plt.title(titulo)

            if eixox:
                ax.set_xlabel(eixox)

            if eixoy:
                ax.set_ylabel(eixoy)

            if eixoz:
                ax.set_zlabel(eixoz)

            if salvar_como:
                plt.savefig(salvar_como)
            else:
                plt.show()

        except Exception as e:
            return e


    def grafico_contorno(x, y, z, titulo=None, eixox=None, eixoy=None, tamanho_d_figura=(8, 6), salvar_como=None):
        try:
            import numpy as np
            import matplotlib.pyplot as plt
            plt.rcParams['toolbar'] = 'None'
            plt.rcParams['toolbar'] = 'None'
            X, Y = np.meshgrid(x, y)
            plt.figure(figsize=tamanho_d_figura)
            plt.contour(X, Y, z)

            if titulo:
                plt.title(titulo)

            if eixox:
                plt.xlabel(eixox)

            if eixoy:
                plt.ylabel(eixoy)

            if salvar_como:
                plt.savefig(salvar_como)
            else:
                plt.show()

        except Exception as e:
            return e

    

    def grafico_polar(angulos, valores, titulo=None, tamanho_d_figura=(8, 6), salvar_como=None):
        try:
            import matplotlib.pyplot as plt
            plt.rcParams['toolbar'] = 'None'
            plt.rcParams['toolbar'] = 'None'
            plt.figure(figsize=tamanho_d_figura)
            plt.polar(angulos, valores)

            if titulo:
                plt.title(titulo)

            if salvar_como:
                plt.savefig(salvar_como)
            else:
                plt.show()

        except Exception as e:
            return e





#Classe de Equações    
class Equacao:
    
    def equacaoPrimeiroGrauEx(a, b, c):
        try:
            if a == 0:
                return "A equação não é do primeiro grau."
            else:
                x = (c - b) / a
                sinal = '+' if b >= 0 else ''
                expl = (
                    f"{a}x {sinal}{b} = {c}, "
                    f"{b} vai trocar de lado e vai no lado do {c}, "
                    f"mais vai trocar de sinal, "
                    f"vai ficar {a}x = {c} - ({sinal}{b}), "
                    f"{a}x = {c-b}, "
                    f"x = {c-b}/{a}, "
                    f"x = {x}"
                )
                return f"{a}x {sinal}{b} = {c}  (x: {x}), --EXPLICAÇÃO--, {expl}"
        except Exception as e:
            return str(e)
        
    def epgEx(a, b, c):
        try:
            if a == 0:
                return "A equação não é do primeiro grau."
            else:
                x = (c - b) / a
                sinal = '+' if b >= 0 else ''
                expl = (
                    f"{a}x {sinal}{b} = {c}, "
                    f"{b} vai trocar de lado e vai no lado do {c}, "
                    f"mais vai trocar de sinal, "
                    f"vai ficar {a}x = {c} - ({sinal}{b}), "
                    f"{a}x = {c-b}, "
                    f"x = {c-b}/{a}, "
                    f"x = {x}"
                )
                return f"{a}x {sinal}{b} = {c}  (x: {x}), --EXPLICAÇÃO--, {expl}"
        except Exception as e:
            return str(e)


    def equacaoSegundoGrauEx(a, b, c):
        try:
            import math

            if a == 0:
                return "A equação não é do segundo grau."

            delta = b ** 2 - 4 * a * c

            if delta < 0:
                return "A equação não possui raízes reais."
            elif delta == 0:
                x = -b / (2 * a)
                return f"A equação possui uma raiz real: x = {x}"
            else:
                sinal_b = '+' if b >= 0 else ''
                sinal_c = '+' if c >= 0 else ''

                x1 = (-b + math.sqrt(delta)) / (2 * a)
                x2 = (-b - math.sqrt(delta)) / (2 * a)

                exp = (
                    f"delta = {b}² - 4 * {a} * {c}, "
                    f"Se delta < 0, a equação não possui raízes reais, "
                    f"Senão, as raízes são:, "
                    f"x = {sinal_b}{b} / (2 * {a}), "
                    f"x1 = ({sinal_b}{b} + √{delta}) / (2 * {a}), "
                    f"x2 = ({sinal_b}{b} - √{delta}) / (2 * {a}), "
                    f"x1 = {x1}, x2 = {x2}"
                )

                return (
                    f"A equação {a}x² {sinal_b}{b}x {sinal_c}{c} = 0 possui duas raízes reais:, "
                    f"x1 = {x1}, x2 = {x2}"
                    f" --EXPLICAÇÃO--, {exp}"
                )
        except Exception as e:
            print("Erro: ", e)
            return "Ocorreu um erro ao calcular a equação de segundo grau."
        

    def esgEx(a, b, c):
        try:
            import math

            if a == 0:
                return "A equação não é do segundo grau."

            delta = b ** 2 - 4 * a * c

            if delta < 0:
                return "A equação não possui raízes reais."
            elif delta == 0:
                x = -b / (2 * a)
                return f"A equação possui uma raiz real: x = {x}"
            else:
                sinal_b = '+' if b >= 0 else ''
                sinal_c = '+' if c >= 0 else ''

                x1 = (-b + math.sqrt(delta)) / (2 * a)
                x2 = (-b - math.sqrt(delta)) / (2 * a)

                exp = (
                    f"delta = {b}² - 4 * {a} * {c}, "
                    f"Se delta < 0, a equação não possui raízes reais, "
                    f"Senão, as raízes são:, "
                    f"x = {sinal_b}{b} / (2 * {a}), "
                    f"x1 = ({sinal_b}{b} + √{delta}) / (2 * {a}), "
                    f"x2 = ({sinal_b}{b} - √{delta}) / (2 * {a}), "
                    f"x1 = {x1}, x2 = {x2}"
                )

                return (
                    f"A equação {a}x² {sinal_b}{b}x {sinal_c}{c} = 0 possui duas raízes reais:, "
                    f"x1 = {x1}, x2 = {x2}"
                    f" --EXPLICAÇÃO--, {exp}"
                )
        except Exception as e:
            print("Erro: ", e)
            return "Ocorreu um erro ao calcular a equação de segundo grau."




    def equacaoPrimeiroGrau(a, b, c):
        try:
            if a == 0:
                return "A equação não é do primeiro grau."
            else:
                x = (c - b) / a
                return x
        except Exception as e:
            return e
        
    def epg(a, b, c):
        try:
            if a == 0:
                return "A equação não é do primeiro grau."
            else:
                x = (c - b) / a
                return x
        except Exception as e:
            return e

    def equacaoSegundoGrau(a, b, c):
        try:
            if a == 0:
                return "A equação não é do segundo grau."

            delta = b ** 2 - 4 * a * c

            if delta < 0:
                return "A equação não possui raízes reais."
            elif delta == 0:
                x = -b / (2 * a)
                return f"A equação possui uma raiz real: x = {x}"
            else:
                x1 = (-b + raiz_quadrada(delta)) / (2 * a)
                x2 = (-b - raiz_quadrada(delta)) / (2 * a)
                return f"A equação possui duas raízes reais: x1 = {x1}, x2 = {x2}"
        except Exception as e:
            return e
        
    def esg(a, b, c):
        try:
            if a == 0:
                return "A equação não é do segundo grau."

            delta = b ** 2 - 4 * a * c

            if delta < 0:
                return "A equação não possui raízes reais."
            elif delta == 0:
                x = -b / (2 * a)
                return f"A equação possui uma raiz real: x = {x}"
            else:
                x1 = (-b + raiz_quadrada(delta)) / (2 * a)
                x2 = (-b - raiz_quadrada(delta)) / (2 * a)
                return f"A equação possui duas raízes reais: x1 = {x1}, x2 = {x2}"
        except Exception as e:
            return e
    
#Classes de Sistema Operacional
class SO:
    def diretorio_atual():
        try:
            import os
            return f"({os.getcwd()})"
        except OSError as e:
            return e

    def lista_arq_dir(caminho:str):
        try:
            import os
            return os.listdir(caminho)
        except OSError:
            return "Esse Caminho é invalido"

    def criar_diretorio(novo_diretorio:str):
        try:
            import os
            os.mkdir(novo_diretorio)
        except OSError as e:
            return e

    def remover_arq(arquivo:str):
        try:
            import os
            if os.path.isfile(arquivo):
                os.remove(arquivo)
            elif os.path.isdir(arquivo):
                return "É um Diretório"
        except OSError as e:
            return e

    def remover_dir(diretorio:str):
        try:
            import os
            if os.path.isdir(diretorio):
                os.remove(diretorio)
            elif os.path.isfile(diretorio):
                return "É um arquivo"
        except OSError as e:
            return e

    def remover_dir_td(diretorio:str):
        try:
            import os
            import shutil
            shutil.rmtree(diretorio)
        except OSError as e:
            return e
        
    def eh_arquivo(caminho:str):
        try:
            import os
            if os.path.isfile(caminho):
                return f"'{caminho}' É um arquivo"
            elif not os.path.isfile(caminho) and os.path.isdir(caminho):
                return f"'{caminho}' Não é um arquivo, é um diretório"
            else:
                return f"Arquivo '{caminho}' Inválido"
        except OSError as e:
            return e
        
    def eh_diretorio(caminho:str):
        try:
            import os
            if os.path.isdir(caminho):
                return f"'{caminho}' É um diretorio"
            elif not os.path.isdir(caminho)  and os.path.isfile(caminho):
                return f"'{caminho}'Não é um diretório, é um arquivo"
            else:
                return f"Diretório '{caminho}' Inválido"
        except OSError as e:
            return e
        

    def versao_python():
        try:
            import sys
            return f'Versão:{sys.version}'
        except SystemError as e:
            return e

    def sistema_operacional():
        try:
            import sys
            return sys.platform
        except SystemError as e: return e
        
    def plataforma():
        try:
            import sys
            pla = [s for s in sys.platform]
            return f'plataforma: {pla}'
        except SystemError as e: return e



    def existe_arq_dir(arquivo_ou_diretorio:str):
        try:
            import os
            if os.path.exists(arquivo_ou_diretorio):
                if os.path.isfile(arquivo_ou_diretorio):
                    return "Este Arquivo existe"
                elif os.path.isdir(arquivo_ou_diretorio):
                    return "Este diretorio existe"
                else:
                    return "Não existe"
            else:
                return "Caminho Inválido"
        except OSError as e:
            return e
        
    def mover_arq_dir(nome_atual:str, caminho:str):
        try:
            import os
            if os.path.exists(nome_atual) and os.path.exists(caminho):
                os.rename(nome_atual, os.path.join(caminho, nome_atual))
                return f"O Arquivo '{nome_atual}' Foi movido pelo diretorio '{caminho}'"
            elif not os.path.exists(nome_atual):
                return f"{nome_atual} Não existe"
            elif not os.path.exists(caminho):
                return f"{caminho} Não existe"
        except OSError as e:
            return e

    def mostra_arq_dire():
         import platform, os
         if platform.system() == "Windows":
            os.system('dir')
         else:
            os.system('ls')

    def mad():
         import platform, os
         if platform.system() == "Windows":
            os.system('dir')
         else:
            os.system('ls')
    
    def criar_arquivo(nome_arquivo:str, conteudo:str):
        try:
            with open(nome_arquivo, 'w') as arquivo:
                arquivo.write(conteudo)
            print(f'Arquivo "{nome_arquivo}" criado com sucesso.')
        except Exception as e:
            return f'Erro ao criar o arquivo: {e}'
    
    def ca(nome_arquivo:str, conteudo:str):
        try:
            with open(nome_arquivo, 'w') as arquivo:
                arquivo.write(conteudo)
            print(f'Arquivo "{nome_arquivo}" criado com sucesso.')
        except Exception as e:
            return f'Erro ao criar o arquivo: {e}'
        
    
        
    def criar_arquivo_(nome_arquivo:str):
        try:
            with open(nome_arquivo, 'w') as arquivo:
                arquivo.write("")
            print(f'Arquivo "{nome_arquivo}" criado com sucesso.')
        except Exception as e:
            return f'Erro ao criar o arquivo: {e}'
    
    def ca_(nome_arquivo:str): #criar arquivo 
        try:
            with open(nome_arquivo, 'w') as arquivo:
                arquivo.write("")
            print(f'Arquivo "{nome_arquivo}" criado com sucesso.')
        except Exception as e:
            return f'Erro ao criar o arquivo: {e}'
        

    def adicionar_conteudo_arquivo(nome_arquivo:str, conteudo:str):
        try:
            with open(nome_arquivo, 'a') as arquivo:
                arquivo.write(conteudo)
            print(f'Conteúdo adicionado ao arquivo "{nome_arquivo}" com sucesso.')
        except Exception as e:
            print(f'Erro ao adicionar conteúdo ao arquivo: {e}')

    def aca(nome_arquivo:str, conteudo:str): # adicionar conteudo arquivo
        try:
            with open(nome_arquivo, 'a') as arquivo:
                arquivo.write(conteudo)
            print(f'Conteúdo adicionado ao arquivo "{nome_arquivo}" com sucesso.')
        except Exception as e:
            print(f'Erro ao adicionar conteúdo ao arquivo: {e}')

    def ler_arquivo(nome_arquivo:str):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                conteudo = arquivo.read()
            return conteudo
        except Exception as e:
            print(f'Erro ao ler o arquivo: {e}')
            return None
        
    def la(nome_arquivo:str): #ler arquivo
        try:
            with open(nome_arquivo, 'r') as arquivo:
                conteudo = arquivo.read()
            return conteudo
        except Exception as e:
            print(f'Erro ao ler o arquivo: {e}')
            return None
    
     
    def ler_arquivo_linhas_lista(nome_arquivo:str):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                linhas = arquivo.readlines()
            return linhas
        except Exception as e:
            print(f'Erro ao ler o arquivo: {e}')
            return None
        
    def lall(nome_arquivo:str): # ler arquivo linhas lista
        try:
            with open(nome_arquivo, 'r') as arquivo:
                linhas = arquivo.readlines()
            return linhas
        except Exception as e:
            print(f'Erro ao ler o arquivo: {e}')
            return None
    

        
    def ler_arquivo_linha_por_linha(nome_arquivo:str):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                for linha in arquivo:
                    print(linha.rstrip())  # rstrip() remove a quebra de linha no final
        except Exception as e:
            print(f'Erro ao ler o arquivo: {e}')

    def lalpl(nome_arquivo:str): #lalpl ler arquivo linha por linha
        try:
            with open(nome_arquivo, 'r') as arquivo:
                for linha in arquivo:
                    print(linha.rstrip())  # rstrip() remove a quebra de linha no final
        except Exception as e:
            print(f'Erro ao ler o arquivo: {e}')

    def abrir_arquivo(arquivo):
        try:
            import os
            os.startfile(arquivo)
        except OSError as e: return e

    def pesquisa_arq(arquivo:str):
        try:
            import glob
            return glob.glob(f'*.{arquivo}')
        except Exception as e: return e

    def remover_td_arq(arquivo):
        try:
            import glob, os
            s = glob.glob(f"*.{arquivo}")
            for i in s:
                os.remove(i)
        except Exception as e: return e
    
    def diretorio_ctssd(diretorio_fonte, destinacao): #ctssd (com tudo seu sub diretorios)
        try:
            import shutil
            shutil.copytree(diretorio_fonte, destinacao)
        except Exception as e: return e

    

        

   
# Classe Trigonometria
class Trigonometria:
    # Função para calcular o seno de um ângulo em radianos
    def seno(angle):
        try:
            import math
            return math.sin(angle)
        except Exception as e:
            return e
        
    # Função para calcular o cosseno de um ângulo em radianos
    def cosseno(angle):
        try:
            import math
            return math.cos(angle)
        except Exception as e:
            return e

    # Função para calcular a tangente de um ângulo em radianos
    def tangente(angle):
        try:
            import math
            return math.tan(angle)
        except Exception as e:
            return e

    # Função para calcular o cosseno hiperbólico de um número
    def cosseno_hiperbolico(num):
        try:
            import math
            return math.cosh(num)
        except Exception as e:
            return e

    # Função para calcular o seno hiperbólico de um número
    def seno_hiperbolico(num):
        try:
            import math
            return math.sinh(num)
        except Exception as e:
            return e

    # Função para calcular a tangente hiperbólica de um número
    def tangente_hiperbolica(num):
        try:
            import math
            return math.tanh(num)
        except Exception as e:
            return e

    # Função para calcular o arco cosseno de um número
    def arco_cosseno(num):
        try:
            import math
            return math.acos(num)
        except Exception as e:
            return e

    # Função para calcular o arco seno de um número
    def arco_seno(num):
        try:
            import math
            return math.asin(num)
        except Exception as e:
            return e

    # Função para calcular o arco tangente de um número
    def arco_tangente(num):
        try:
            import math
            return math.atan(num)
        except Exception as e:
            return e

    # Função para calcular o arco tangente de um número com dois argumentos (y, x)
    def arco_tangente2(y, x):
        try:
            import math
            return math.atan2(y, x)
        except Exception as e:
            return e

#Classe de Estatistica
class Estatistica:
    def media(*args):
        try:
            return sum(args) / len(args)
        except Exception as e:
            return e

    def mediana(*args):
        try:
            sorted_args = sorted(args)
            n = len(sorted_args)
            if n % 2 == 0:
                return (sorted_args[n // 2 - 1] + sorted_args[n // 2]) / 2
            else:
                return sorted_args[n // 2]
        except Exception as e:
            return e

    def moda(*args):
        try:
            counter = {}
            for num in args:
                if num in counter:
                    counter[num] += 1
                else:
                    counter[num] = 1
            max_count = max(counter.values())
            return [num for num, count in counter.items() if count == max_count]
        except Exception as e:
            return e

    def desvio_padrao(self,*args):
        try:
            import math
            n = len(args)
            if n == 0:
                raise ValueError("A lista de valores não pode ser vazia.")
            mean = sum(args) / n
            squared_diff_sum = sum((x - mean) ** 2 for x in args)
            variance = squared_diff_sum / n
            return math.sqrt(variance)
        except Exception as e:
            return e

    def desvio_medio(*args):
        try:
            n = len(args)
            if n == 0:
                raise ValueError("A lista de valores não pode ser vazia.")
            return sum(abs(x - sum(args) / n) for x in args) / n
        except Exception as e:
            return e

    def variancia(*args):
        try:
            n = len(args)
            if n == 0:
                raise ValueError("A lista de valores não pode ser vazia.")
            mean = sum(args) / n
            squared_diff_sum = sum((x - mean) ** 2 for x in args)
            return squared_diff_sum / n
        except Exception as e:
            return e

    def comparar(a, b):
        try:
            if len(a) != len(b):
                raise ValueError("As listas de valores devem ter o mesmo tamanho.")
            n = len(a)
            diff_sum = sum(abs(a[i] - b[i]) for i in range(n))
            return diff_sum / n
        except Exception as e:
            return e

    def media_ponderada(valores, pesos):
        try:
            if len(valores) != len(pesos):
                raise ValueError("As listas de valores e pesos devem ter o mesmo tamanho.")
            weighted_sum = sum(valores[i] * pesos[i] for i in range(len(valores)))
            sum_of_weights = sum(pesos)
            return weighted_sum / sum_of_weights
        except Exception as e:
            return e

    def media_geometrica(*args):
        try:
            product = 1
            for num in args:
                product *= num
            return product ** (1 / len(args))
        except Exception as e:
            return e

    def media_quadratica(*args):
        try:
            import math
            squared_sum = sum(x ** 2 for x in args)
            return math.sqrt(squared_sum / len(args))
        except Exception as e:
            return e

    def intervalo_medio(*args):
        try:
            sorted_args = sorted(args)
            return (sorted_args[0] + sorted_args[-1]) / 2
        except Exception as e:
            return e

    def intervalo_medio_entre_dois_numeros(a, b):
        try:
            return (a + b) / 2
        except Exception as e:
            return e

    def amplitude(*args):
        try:
            return max(args) - min(args)
        except Exception as e:
            return e

    def quartis(self, *args):
        try:
            import statistics
            q1 = statistics.percentile(args, 25)
            q2 = statistics.median(args)
            q3 = statistics.percentile(args, 75)
            return q1, q2, q3
        except Exception as e:
            return e

    def amplitude_interquartil(self, *args):
        try:
            q1, _, q3 = self.quartis(*args)
            return q3 - q1
        except Exception as e:
            return e

    

    def coeficiente_correlacao(x, y):
        try:
            from scipy import stats
            import math
            if len(x) != len(y):
                raise ValueError("As listas de valores devem ter o mesmo tamanho.")
            n = len(x)
            sum_xy = sum(x[i] * y[i] for i in range(n))
            sum_x = sum(x)
            sum_y = sum(y)
            sum_x_squared = sum(x[i] ** 2 for i in range(n))
            sum_y_squared = sum(y[i] ** 2 for i in range(n))
            numerator = n * sum_xy - sum_x * sum_y
            denominator = math.sqrt((n * sum_x_squared - sum_x ** 2) * (n * sum_y_squared - sum_y ** 2))
            return numerator / denominator
        except Exception as e:
            return e

    def regressao_linear(x, y):
        try:
            if len(x) != len(y):
                raise ValueError("As listas de valores devem ter o mesmo tamanho.")
            n = len(x)
            sum_x = sum(x)
            sum_y = sum(y)
            sum_x_squared = sum(x[i] ** 2 for i in range(n))
            sum_xy = sum(x[i] * y[i] for i in range(n))

            a = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
            b = (sum_y - a * sum_x) / n

            return a, b
        except Exception as e:
            return e

    def coeficiente_variacao(*args):
        try:
            import statistics
            mean = statistics.mean(args)
            std_deviation = statistics.stdev(args)
            return (std_deviation / mean) * 100
        except Exception as e:
            return e

    def media_harmonica(*args):
        try:
            reciprocal_sum = sum(1 / num for num in args)
            return len(args) / reciprocal_sum
        except Exception as e:
            return e
        
    def distribuicao_frequencia(dados, num_classes):
        try:
            sorted_data = sorted(dados)
            min_value = sorted_data[0]
            max_value = sorted_data[-1]
            range_value = max_value - min_value
            class_width = range_value / num_classes

            frequency_table = {}
            for i in range(num_classes):
                lower_bound = min_value + i * class_width
                upper_bound = lower_bound + class_width
                frequency_table[(lower_bound, upper_bound)] = 0

            for value in sorted_data:
                for interval in frequency_table.keys():
                    lower_bound, upper_bound = interval
                    if lower_bound <= value < upper_bound:
                        frequency_table[interval] += 1
                        break

            return frequency_table
        except Exception as e:
            return e

    def intervalo_confianca(dados, nivel_confianca):
        try:
            import statistics
            from scipy import stats
            import math
            n = len(dados)
            mean = statistics.mean(dados)
            std_deviation = statistics.stdev(dados)
            t_value = stats.t.ppf((1 + nivel_confianca) / 2, n - 1)
            margin_of_error = t_value * (std_deviation / math.sqrt(n))
            lower_bound = mean - margin_of_error
            upper_bound = mean + margin_of_error
            return lower_bound, upper_bound
        except Exception as e:
            return e

    def coeficiente_assimetria(*args):
        try:
            import math
            n = len(args)
            mean = sum(args) / n
            variance = sum((x - mean) ** 2 for x in args) / n
            std_deviation = math.sqrt(variance)
            cubed_deviations = [(num - mean) ** 3 for num in args]
            sum_cubed_deviations = sum(cubed_deviations)
            skewness = (sum_cubed_deviations / (n * std_deviation ** 3))
            return skewness
        except Exception as e:
            return e


    def curtose(*args):
        try:
            n = len(args)
            mean = sum(args) / n
            variance = sum((x - mean) ** 2 for x in args) / n
            fourth_power_deviations = [(num - mean) ** 4 for num in args]
            sum_fourth_power_deviations = sum(fourth_power_deviations)
            kurtosis = (sum_fourth_power_deviations / (n * variance ** 2)) - 3
            return kurtosis
        except Exception as e:
            return e


    def coeficiente_correlacao_pearson(x, y):
        try:
            import math
            if len(x) != len(y):
                raise ValueError("As listas de valores devem ter o mesmo tamanho.")
            n = len(x)
            sum_x = sum(x)
            sum_y = sum(y)
            sum_x_squared = sum(x[i] ** 2 for i in range(n))
            sum_y_squared = sum(y[i] ** 2 for i in range(n))
            sum_xy = sum(x[i] * y[i] for i in range(n))

            numerator = n * sum_xy - sum_x * sum_y
            denominator = math.sqrt((n * sum_x_squared - sum_x ** 2) * (n * sum_y_squared - sum_y ** 2))
            pearson_correlation = numerator / denominator
            return pearson_correlation
        except Exception as e:
            return e

   

    def teste_t(amostra1, amostra2):
        try:
            import math
            if len(amostra1) != len(amostra2):
                raise ValueError("As amostras devem ter o mesmo tamanho.")

            n1 = len(amostra1)
            n2 = len(amostra2)

            mean1 = sum(amostra1) / n1
            mean2 = sum(amostra2) / n2

            variance1 = sum((x - mean1) ** 2 for x in amostra1) / (n1 - 1)
            variance2 = sum((x - mean2) ** 2 for x in amostra2) / (n2 - 1)

            pooled_variance = ((n1 - 1) * variance1 + (n2 - 1) * variance2) / (n1 + n2 - 2)
            pooled_std_deviation = math.sqrt(pooled_variance)

            t_value = (mean1 - mean2) / (pooled_std_deviation * math.sqrt(1 / n1 + 1 / n2))
            return t_value
        except Exception as e:
            return e


    def teste_qui_quadrado(freq_obs, freq_esp):
        try:
            if len(freq_obs) != len(freq_esp):
                raise ValueError("As tabelas de frequência devem ter o mesmo tamanho.")
            n = len(freq_obs)
            chi_squared = sum((freq_obs[i] - freq_esp[i]) ** 2 / freq_esp[i] for i in range(n))
            return chi_squared
        except Exception as e:
            return e

    def analise_variancia(*args):
        try:
            num_amostras = len(args)
            sizes = [len(amostra) for amostra in args]
            grand_mean = sum(sum(amostra) for amostra in args) / sum(sizes)
            total_ss = sum(sum((x - grand_mean) ** 2 for x in amostra) for amostra in args)
            df_total = sum(size - 1 for size in sizes)
            df_between = num_amostras - 1
            df_within = df_total - df_between
            ss_between = sum(size * (sum(amostra) / size - grand_mean) ** 2 for size, amostra in zip(sizes, args))
            ms_between = ss_between / df_between
            ss_within = total_ss - ss_between
            ms_within = ss_within / df_within
            f_value = ms_between / ms_within
            return f_value
        except Exception as e:
            return e
        
    

    def teste_normalidade(amostra, alpha=0.05):
        import numpy as np
        from scipy.stats import chi2
        n = len(amostra)
        mean = np.mean(amostra)
        std_deviation = np.std(amostra, ddof=1)
        z_score = (amostra - mean) / std_deviation
        squared_z_score = z_score ** 2
        chi_square = np.sum(squared_z_score)
        critical_value = chi2.ppf(1 - alpha, df=n - 1)

        return chi_square <= critical_value
    
    def teste_homogeneidade(*grupos, alpha=0.05):
        from scipy.stats import f
        import numpy as np
        n_grupos = len(grupos)
        n_total = np.sum([len(grupo) for grupo in grupos])
        mean_total = np.mean(np.concatenate(grupos))
        squared_deviations_total = np.sum([(x - mean_total) ** 2 for grupo in grupos for x in grupo])
        squared_deviations_between = np.sum([len(grupo) * (np.mean(grupo) - mean_total) ** 2 for grupo in grupos])

        df_between = n_grupos - 1
        df_within = n_total - n_grupos

        mean_squared_deviations_between = squared_deviations_between / df_between
        mean_squared_deviations_within = squared_deviations_total / df_within

        f_statistic = mean_squared_deviations_between / mean_squared_deviations_within
        critical_value = f.ppf(1 - alpha, dfn=df_between, dfd=df_within)

        return f_statistic <= critical_value

#Classe de Calculo
class Calculo:
    def newton_raphson(funcao, derivada, x0, tolerancia=1e-6, max_iter=100):
        x = x0
        iteracoes = 0
        while abs(funcao(x)) > tolerancia and iteracoes < max_iter:
            x = x - funcao(x) / derivada(x)
            iteracoes += 1
        return x

    def derivada(expressao, variavel):
        from sympy import symbols, diff
        x = symbols(variavel)
        return diff(expressao, x)


    def integral_definida(expressao, variavel, limite_inferior, limite_superior):
        from sympy import symbols, integrate
        x = symbols(variavel)
        return integrate(expressao, (x, limite_inferior, limite_superior))


    def integral_indefinida(expressao, variavel):
        from sympy import symbols, integrate
        x = symbols(variavel)
        return integrate(expressao, x)


    
    def limite(expressao, variavel, ponto):
        from sympy import symbols, limit
        x = symbols(variavel)
        return limit(expressao, x, ponto)


    def derivada_parcial(expressao, variaveis):
        from sympy import symbols, diff
        vars = symbols(variaveis)
        return diff(expressao, *vars)

    
    def laplace(expressao, variavel, s):
        from sympy import symbols, laplace_transform
        t = symbols(variavel)
        return laplace_transform(expressao, t, s)



    def inversa_laplace(expressao, s, t):
        from sympy import symbols, inverse_laplace_transform
        t = symbols(t)
        return inverse_laplace_transform(expressao, s, t)



   
    def transformada_fourier(expressao, variavel, w):
        from sympy import symbols, fourier_transform
        t = symbols(variavel)
        return fourier_transform(expressao, t, w)

    

    def inversa_fourier(expressao, w, t):
        from sympy import symbols, inverse_fourier_transform
        w = symbols(w)
        return inverse_fourier_transform(expressao, w, t)


    def soma_riemann(expressao, variavel, limite_inferior, limite_superior, numero_particoes):
        from sympy import symbols, summation
        x = symbols(variavel)
        delta_x = (limite_superior - limite_inferior) / numero_particoes
        pontos = [limite_inferior + i * delta_x for i in range(numero_particoes)]
        return summation(expressao, (x, pontos[0], pontos[-1]), delta_x)

    def produto_riemann(expressao, variavel, limite_inferior, limite_superior, numero_particoes):
        from sympy import symbols, product
        x = symbols(variavel)
        delta_x = (limite_superior - limite_inferior) / numero_particoes
        pontos = [limite_inferior + i * delta_x for i in range(numero_particoes)]
        return product(expressao, (x, pontos[0], pontos[-1]), delta_x)

    def limite_lateral(expressao, variavel, ponto, lado='right'):
        from sympy import symbols, limit
        x = symbols(variavel)
        return limit(expressao, x, ponto, dir=lado)


    def derivada_numerica_progressiva(expressao, variavel, ponto, h=1e-6):
        from sympy import symbols
        x = symbols(variavel)
        f_x = expressao.subs(x, ponto)
        f_xh = expressao.subs(x, ponto + h)
        return (f_xh - f_x) / h


    def derivada_numerica_regressiva(expressao, variavel, ponto, h=1e-6):
        from sympy import symbols
        x = symbols(variavel)
        f_x = expressao.subs(x, ponto)
        f_xh = expressao.subs(x, ponto - h)
        return (f_x - f_xh) / h



    def derivada_numerica_central(expressao, variavel, ponto, h=1e-6):
        from sympy import symbols
        x = symbols(variavel)
        f_xh = expressao.subs(x, ponto + h)
        f_xh2 = expressao.subs(x, ponto - h)
        return (f_xh - f_xh2) / (2 * h)


  
    def integral_numerica_trapezio(expressao, variavel, limite_inferior, limite_superior, numero_particoes):
        from sympy import symbols
        x = symbols(variavel)
        h = (limite_superior - limite_inferior) / numero_particoes
        pontos = [limite_inferior + i * h for i in range(numero_particoes + 1)]
        integral = 0
        for i in range(1, numero_particoes):
            integral += expressao.subs(x, pontos[i])
        integral += (expressao.subs(x, limite_inferior) + expressao.subs(x, limite_superior)) / 2
        integral *= h
        return integral



    def integral_numerica_simpson(expressao, variavel, limite_inferior, limite_superior, numero_particoes):
        from sympy import symbols
        x = symbols(variavel)
        h = (limite_superior - limite_inferior) / numero_particoes
        pontos = [limite_inferior + i * h for i in range(numero_particoes + 1)]
        integral = 0
        for i in range(1, numero_particoes):
            if i % 2 == 0:
                integral += 2 * expressao.subs(x, pontos[i])
            else:
                integral += 4 * expressao.subs(x, pontos[i])
        integral += expressao.subs(x, limite_inferior) + expressao.subs(x, limite_superior)
        integral *= h / 3
        return integral
  

    def serie_taylor(expressao, variavel, ponto, ordem):
        from sympy import symbols, series
        x = symbols(variavel)
        return series(expressao, x, x0=ponto, n=ordem).removeO()

    

    def transformada_laplace(expressao, variavel, s):
        from sympy import symbols, laplace_transform
        t = symbols(variavel)
        return laplace_transform(expressao, t, s, noconds=True)


  

    def inversa_transformada_laplace(expressao, variavel, t):
        from sympy import symbols, inverse_laplace_transform
        s = symbols(variavel)
        return inverse_laplace_transform(expressao, s, t)
    

#Classe de Matrize
class Matrize:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __str__(self):
        return ", ".join([" ".join(map(str, row)) for row in self.data])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("As matrizes devem ter o mesmo tamanho para soma.")
        
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrize(result)
    
    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("As matrizes devem ter o mesmo tamanho para subtração.")
        
        result = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrize(result)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = [[self.data[i][j] * other for j in range(self.cols)] for i in range(self.rows)]
        elif isinstance(other, Matrize):
            if self.cols != other.rows:
                raise ValueError("O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz para multiplicação.")
            
            result = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) for j in range(other.cols)] for i in range(self.rows)]
        else:
            raise TypeError("Multiplicação não suportada entre matriz e outro tipo.")
        
        return Matrize(result)

    def transposta(self):
        result = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return Matrize(result)

    def determinante(self):
        if self.rows != self.cols:
            raise ValueError("O determinante só pode ser calculado para matrizes quadradas.")
        
        return self._determinant_recursive(self.data)

    def _determinante_recursive(self, matrix):
        if len(matrix) == 1:
            return matrix[0][0]
        elif len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        det = 0
        for j in range(len(matrix)):
            submatrix = [row[:j] + row[j+1:] for row in matrix[1:]]
            sub_det = self._determinant_recursive(submatrix)
            det += matrix[0][j] * sub_det * (-1 if j % 2 != 0 else 1)

        return det
    def inversa(self, matriz):
        try:
            from mpmath import mp
            mp.dps = 5
            result = mp.inverse(matriz)
            return result
        except Exception as e:
            return e
    
    
    def calcular_autovalores_autovetores(matriz):
        try:
            from mpmath import mp
            # Converter a matriz para o formato mpmath
            A = mp.matrix(matriz)
            
            # Calcular os autovalores e autovetores usando a função eig()
            autovalores, autovetores = mp.eig(A)
            
            # Converter os resultados para listas para facilitar a manipulação
            autovalores = [complex(val) for val in autovalores]
            autovetores = [[complex(val) for val in vetor] for vetor in autovetores]
            
            return autovalores, autovetores
        except Exception as e:
            return e


#Classe de AlgebraLinear
class AlgebraLinear:
    # Função para multiplicar uma matriz por um escalar
    @staticmethod
    def multiplicar_matriz_por_escalar(matriz, escalar):
        resultado = []
        for linha in matriz:
            nova_linha = [elemento * escalar for elemento in linha]
            resultado.append(nova_linha)
        return resultado

    # Função para dividir uma matriz por um escalar
    @staticmethod
    def dividir_matriz_por_escalar(matriz, escalar):
        if escalar == 0:
            raise ValueError("Não é possível dividir uma matriz por zero.")
        return AlgebraLinear.multiplicar_matriz_por_escalar(matriz, 1 / escalar)

    # Função para multiplicar uma matriz por um vetor
    @staticmethod
    def multiplicar_matriz_por_vetor(matriz, vetor):
        if len(matriz[0]) != len(vetor):
            raise ValueError("O número de colunas da matriz deve ser igual ao tamanho do vetor.")
        resultado = []
        for linha in matriz:
            soma = sum(elemento * vetor[i] for i, elemento in enumerate(linha))
            resultado.append(soma)
        return resultado


    # Função para resolver um sistema de equações lineares utilizando matrizes
    @staticmethod
    def resolver_sistema_linear(coeficientes, constantes):
        import copy
        matriz_coeficientes = copy.deepcopy(coeficientes)
        matriz_constantes = [[float(constante)] for constante in constantes]
        inversa_coeficientes = AlgebraLinear.matriz_inversa(matriz_coeficientes)

        # Multiplicar a matriz inversa pelos vetores constantes corretamente
        solucao = AlgebraLinear.multiplicar_matriz(inversa_coeficientes, matriz_constantes)

        return [f"{item[0]:.2f}" for item in solucao]


    # Função para calcular a matriz inversa
    @staticmethod
    def matriz_inversa(matriz):
        n = len(matriz)
        identidade = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        matriz_aumentada = [linha + identidade[i] for i, linha in enumerate(matriz)]
        for i in range(n):
            pivo = matriz_aumentada[i][i]
            if pivo == 0:
                raise ValueError("A matriz não possui inversa.")
            for j in range(i, n * 2):
                matriz_aumentada[i][j] /= pivo
            for k in range(n):
                if k != i:
                    fator = matriz_aumentada[k][i]
                    for j in range(i, n * 2):
                        matriz_aumentada[k][j] -= fator * matriz_aumentada[i][j]
        matriz_inversa = [linha[n:] for linha in matriz_aumentada]
        return matriz_inversa

    # Função para elevar uma matriz a uma potência inteira
    @staticmethod
    def potencia_matriz(matriz, potencia):
        if len(matriz) != len(matriz[0]):
            raise ValueError("A matriz deve ser quadrada para ser elevada a uma potência.")
        if potencia == 0:
            n = len(matriz)
            return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        if potencia < 0:
            matriz = AlgebraLinear.matriz_inversa(matriz)
            potencia *= -1
        resultado = matriz
        for _ in range(potencia - 1):
            resultado = AlgebraLinear.multiplicar_matriz(resultado, matriz)
        return resultado


    def decomposicao_LU(matriz):
        from mpmath import mp
        if len(matriz) != len(matriz[0]):
            raise ValueError("A matriz deve ser quadrada para a decomposição LU.")
        
        A = mp.matrix(matriz)
        L, U = A.LUdecomposition()
        return [[complex(val) for val in linha] for linha in L], [[complex(val) for val in linha] for linha in U]

    # Função para realizar a decomposição QR de uma matriz
    @staticmethod
    def fatoracao_QR(matriz):
        from mpmath import mp
        A = mp.matrix(matriz)
        Q, R = A.QR()
        return [[complex(val) for val in linha] for linha in Q], [[complex(val) for val in linha] for linha in R]

    # Função para realizar a decomposição de Cholesky de uma matriz simétrica positiva definida
    @staticmethod 
    def decomposicao_cholesky(matriz):
        from mpmath import mp
        if len(matriz) != len(matriz[0]):
            raise ValueError("A matriz deve ser quadrada para a decomposição de Cholesky.")
        
        A = mp.matrix(matriz)
        L = A.cholesky()
        return [[complex(val) for val in linha] for linha in L]

    # Função para resolver um sistema de equações lineares usando o método de Gauss-Seidel
    @staticmethod
    def gauss_seidel(A, b, x0, max_iter=100, tolerancia=1e-10):
        from mpmath import mp
        A = mp.matrix(A)
        b = mp.matrix(b)
        x0 = mp.matrix(x0)
        n = len(x0)
        
        x = x0
        for iteracao in range(max_iter):
            x_anterior = x.copy()
            for i in range(n):
                soma = mp.mpc(0)
                for j in range(n):
                    if i != j:
                        soma += A[i, j] * x[j]
                x[i] = (b[i] - soma) / A[i, i]
            
            erro = mp.norm(x - x_anterior, 'inf')
            if erro < tolerancia:
                print(f'Convergiu em {iteracao + 1} iterações.')
                return [complex(val) for val in x]
        
        print('Não convergiu após as iterações máximas.')
        return [complex(val) for val in x]


    @staticmethod
    def interpolar_polinomial(pontos):
        n = len(pontos)
        if n < 2:
            raise ValueError("A interpolação polinomial requer pelo menos 2 pontos.")
        
        # Separa os pontos em listas de x e y
        x, y = zip(*pontos)
        
        # Implementação da interpolação polinomial utilizando o método de Lagrange
        def lagrange_basis(i):
            def basis(x_value):
                result = 1.0
                for j in range(n):
                    if i != j:
                        result *= (x_value - x[j]) / (x[i] - x[j])
                return result
            return basis

        def polynomial_interpolation(x_value):
            interpolation = 0.0
            for i in range(n):
                interpolation += y[i] * lagrange_basis(i)(x_value)
            return interpolation
        
        return polynomial_interpolation

    # Função para ajuste de curvas usando regressão linear
    @staticmethod
    def regressao_linear(pontos):
        n = len(pontos)
        if n < 2:
            raise ValueError("O ajuste de curvas por regressão linear requer pelo menos 2 pontos.")
        # Separa os pontos em listas de x e y
        x, y = zip(*pontos)

        mean_x = sum(x) / n
        mean_y = sum(y) / n

        sum_xy = sum(xi * yi for xi, yi in pontos)
        sum_x_squared = sum(xi ** 2 for xi in x)

        slope = (n * sum_xy - sum(x) * sum(y)) / (n * sum_x_squared - sum(x) ** 2)
        intercept = mean_y - slope * mean_x

        def linear_regression(x_value):
            return slope * x_value + intercept
        
        return linear_regression

    # Função para calcular integrais definidas usando o método do trapézio
    @staticmethod
    def integracao_trapezio(funcao, limite_inferior, limite_superior, numero_trapezios):
        if numero_trapezios < 1:
            raise ValueError("O número de trapézios deve ser pelo menos 1.")

        h = (limite_superior - limite_inferior) / numero_trapezios
        integral = (funcao(limite_inferior) + funcao(limite_superior)) / 2

        for i in range(1, numero_trapezios):
            x = limite_inferior + i * h
            integral += funcao(x)

        integral *= h
        return integral

    # Função para resolver equações diferenciais usando o método de Euler
    @staticmethod
    def metodo_euler(derivada, condicao_inicial, intervalo, passo):
        t = intervalo[0]
        y = condicao_inicial
        resultado = [(t, y)]
        
        while t + passo <= intervalo[1]:
            y += passo * derivada(t, y)
            t += passo
            resultado.append((t, y))
        
        return resultado
    
    @staticmethod
    def multiplicar_matriz(matriz1, matriz2):
        if len(matriz1[0]) != len(matriz2):
            raise ValueError("O número de colunas da matriz1 deve ser igual ao número de linhas da matriz2.")
        resultado = []
        for i in range(len(matriz1)):
            linha_resultado = []
            for j in range(len(matriz2[0])):
                elemento = sum(matriz1[i][k] * matriz2[k][j] for k in range(len(matriz2)))
                linha_resultado.append(elemento)
            resultado.append(linha_resultado)
        return resultado
    
    def produto_interno_complexo(self, v1, v2):
    # Calcula o produto interno entre dois vetores complexos
        return sum(v1_i.conjugate() * v2_i for v1_i, v2_i in zip(v1, v2))


    def vetor_conjugado_complexo(v):
        # Retorna o vetor conjugado de um vetor complexo
        return [v_i.conjugate() for v_i in v]
    


    def transformacao_linear(matriz, vetor):
        try:
            import numpy as np
        # Realiza a multiplicação de uma matriz por um vetor para representar a transformação linear
            return np.dot(matriz, vetor)
        except Exception as e:
            return e
    
    
    def eh_diagonalizavel(self,matriz):
        try:
            import numpy as np
            # Verifica se uma matriz é diagonalizável
            autovalores, _ = np.linalg.eig(matriz)
            return len(set(autovalores)) == matriz.shape[0]
        except Exception as e:
            return e
        
    @staticmethod
    def diagonalizar_matriz(self,matriz):
        try:
            import numpy as np
            # Diagonaliza uma matriz e retorna a matriz diagonal e a matriz de autovetores
            if self.eh_diagonalizavel(matriz):
                autovalores, autovetores = np.linalg.eig(matriz)
                matriz_diagonal = np.diag(autovalores)
                return autovetores, matriz_diagonal, np.linalg.inv(autovetores)
            else:
                raise ValueError("A matriz não é diagonalizável.")
        except Exception as e:
            return  e
        
    def sao_ortogonais(self, v1, v2):
        import math
    # Verifica se dois vetores são ortogonais
        return math.isclose(self.produto_interno_complexo(v1, v2), 0)

    def projecao_ortogonal(self, v, u):
        try:
        # Calcula a projeção ortogonal do vetor v no vetor u
            fator = self.produto_interno_complexo(v, u) / self.produto_interno_complexo(u, u)
            return [fator * u_i for u_i in u]
        except Exception as e:
            return e

    

    def decomposicao_valores_singulares(matriz):
        try:
            import numpy as np
            # Realiza a decomposição em valores singulares de uma matriz
            U, S, Vh = np.linalg.svd(matriz)
            return U, np.diag(S), Vh
        except Exception as e:
            return e
    
    

    def autovalores_generalizados(*args):
        try:
            import numpy as np
            # Verifica se foi fornecido pelo menos duas matrizes
            if len(args) < 2:
                raise ValueError("É necessário fornecer pelo menos duas matrizes.")
            
            # Calcula os autovalores generalizados para o par de matrizes
            eigenvalues, _ = np.linalg.eig(args[0], args[1])
            return eigenvalues
        except Exception as e:
            return str(e)  
    

    def decomposicao_espectral(matriz):
        try:
            import numpy as np
            # Realiza a decomposição espectral de uma matriz simétrica
            autovalores, autovetores = np.linalg.eigh(matriz)
            matriz_diagonal = np.diag(autovalores)
            return autovetores, matriz_diagonal, np.linalg.inv(autovetores)
        except Exception as e:
            return e
        
    def interpolacao_polinomial(pontos):
        try:
            import numpy as np
            # Realiza a interpolação polinomial de um conjunto de pontos
            x, y = zip(*pontos)
            coeficientes = np.polyfit(x, y, len(pontos) - 1)
            return np.poly1d(coeficientes)
        except Exception as e:
            return e

    def ajuste_mmq(x, y, grau):
        try:
            import numpy as np
            # Realiza o ajuste de curvas por mínimos quadrados a um polinômio de grau 'grau'
            coeficientes = np.polyfit(x, y, grau)
            return np.poly1d(coeficientes)
        except Exception as e:
            return e
   

    def decomposicao_svd(matriz):
        try:
            import numpy as np
            # Realiza a decomposição de valores singulares (SVD) de uma matriz
            U, S, Vt = np.linalg.svd(matriz)
            return U, S, Vt
        except Exception as e:
            return e
        

    def pseudo_inversa_moore_penrose(matriz):
        try:
            import numpy as np
            # Calcula a pseudo-inversa de Moore-Penrose de uma matriz
            return np.linalg.pinv(matriz)
        except Exception as e:
            return e
    

    def determinante_vandermonde(vetor):
        try:     
            import numpy as np
            # Calcula o determinante de uma matriz de Vandermonde construída a partir de um vetor
            return np.linalg.det(np.vander(vetor))
        except Exception as e:
            return e

    

    

    def produto_tensorial(*args):
        try:
            import numpy as np
            if len(args) < 2:
                raise ValueError("A função requer pelo menos duas matrizes como argumento.")
            
            # Inicializa a matriz resultante com a primeira matriz
            resultado = args[0]

            # Calcula o produto tensorial com as matrizes restantes
            for matriz in args[1:]:
                resultado = np.kron(resultado, matriz)

            return resultado
        except Exception as e:
            return str(e)  # Convertendo a exceção para string para retornar a mensagem de erro

    

    def norma_matricial(matriz, ordem=2):
        try:
            import numpy as np
            # Calcula a norma matricial de uma matriz
            return np.linalg.norm(matriz, ord=ordem)
        except Exception as e:
            return e


    

    def matriz_cofatora(matriz):
        try:
            import numpy as np
            # Calcula a matriz cofatora de uma matriz quadrada
            return np.linalg.inv(matriz).T * np.linalg.det(matriz)
        except Exception as e:
            return e
   
    
        

    def traco_matriz(matriz):
        try:
            import numpy as np
            # Calcula o traço de uma matriz (soma dos elementos da diagonal principal)
            return np.trace(matriz)
        except Exception as e:
            return e
        
   

    def decomposicao_schur(matriz):
        try:
            import numpy as np
            # Calcula a Decomposição de Schur de uma matriz
            T, Q = np.linalg.schur(matriz)
            return T, Q
        except Exception as e:
            return e

    

    def pseudoinversa_matriz(matriz):
        try:
            import numpy as np
            # Calcula a pseudoinversa de uma matriz
            return np.linalg.pinv(matriz)
        except Exception as e:
            return e
        

    def exp_matriz_comutador(*matrizes):
        try:
            import numpy as np
            if len(matrizes) < 2:
                raise ValueError("Pelo menos duas matrizes devem ser fornecidas.")
                
            comutador = np.zeros_like(matrizes[0])
            for i in range(len(matrizes) - 1):
                for j in range(i + 1, len(matrizes)):
                    comutador += np.dot(matrizes[i], matrizes[j]) - np.dot(matrizes[j], matrizes[i])
                    
            return np.linalg.expm(comutador)
        except Exception as e:
            return e
        
    

    def decomposicao_jordan(matriz):
        try:
            import numpy as np
            # Calcula a Decomposição de Jordan de uma matriz
            blocos, jordan_form = np.linalg.jordan(matriz)
            return blocos, jordan_form
        except Exception as e:
            return e
        
    

    def resolver_sistema_nao_linear(funcoes, valores_iniciais):
        try:
            import numpy as np
            from scipy.optimize import fsolve
            # Resolve um sistema de equações não-lineares usando o método de Newton-Raphson
            return fsolve(funcoes, valores_iniciais)
        except Exception as e:
            return e
        
    

    def e_conexo(grafo):
        try:
            import networkx as nx
            G = nx.Graph(grafo)
            return nx.is_connected(G)
        except Exception as e:
            return e

            
#Classe de Geometria
class Geometria:
  
    # Distância entre dois pontos no plano 2D
    def distancia_pontos_2D(x1, y1, x2, y2):
        import math
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # Distância entre dois pontos no espaço 3D
    def distancia_pontos_3D(x1, y1, z1, x2, y2, z2):
        import math
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

    # Área de um triângulo no plano 2D (fórmula de Heron)
    def area_triangulo_2D(a, b, c):
        import math
        s = (a + b + c) / 2  # Semiperímetro
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    # Volume de um cubo
    def volume_cubo(aresta):
        return aresta**3

    # Volume de um paralelepípedo
    def volume_paralelepipedo(a, b, c):
        return a * b * c

    # Volume de uma esfera
    def volume_esfera(raio):
        import math
        return (4/3) * math.pi * raio**3

    # Área de uma circunferência
    def area_circunferencia(raio):
        import math
        return math.pi * raio**2

    # Área de um círculo
    def area_circulo(raio):
        import math
        return 2 * math.pi * raio

    # Área de um triângulo no espaço 3D (fórmula de Heron)
    def area_triangulo_3D(a, b, c):
        import math
        s = (a + b + c) / 2  # Semiperímetro
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    # Ângulo entre dois vetores no espaço 3D
    def angulo_entre_vetores_3D(vetor1, vetor2):
        import math
        import numpy as np
        norma_vetor1 = np.linalg.norm(vetor1)
        norma_vetor2 = np.linalg.norm(vetor2)
        if norma_vetor1 == 0 or norma_vetor2 == 0:
            raise ValueError("Os vetores não podem ser nulos.")
        dot_product = np.dot(vetor1, vetor2)
        return math.acos(dot_product / (norma_vetor1 * norma_vetor2))

    # Área de um retângulo
    def area_retangulo(base, altura):
        return base * altura

    # Área de um quadrado
    def area_quadrado(lado):
        return lado**2

    # Volume de um cilindro
    def volume_cilindro(raio_base, altura):
        import math
        return math.pi * raio_base**2 * altura

    # Volume de um cone
    def volume_cone(raio_base, altura):
        import math
        return (1/3) * math.pi * raio_base**2 * altura

    # Volume de uma pirâmide
    def volume_piramide(area_base, altura):
        return (1/3) * area_base * altura

    # Área de um paralelogramo
    def area_paralelogramo(base, altura):
        return base * altura

    # Área de um trapézio
    def area_trapezio(base_maior, base_menor, altura):
        return (base_maior + base_menor) * altura / 2

    # Área de um cilindro
    def area_cilindro(raio_base, altura):
        import math
        return 2 * math.pi * raio_base * (raio_base + altura)

    # Área de um cone
    def area_cone(raio_base, geratriz):
        import math
        return math.pi * raio_base * (raio_base + geratriz)

    # Volume de um prisma retangular
    def volume_prisma_retangular(area_base, altura):
        return area_base * altura

    # Volume de uma esfera a partir de sua superfície
    def volume_esfera_superficie(area_superficie):
        import math
        return (4/3) * math.pi * (area_superficie / (4 * math.pi))**(3/2)

    # Volume de um tetraedro regular
    def volume_tetraedro_regular(aresta):
        import math
        return (aresta**3) / (6 * math.sqrt(2))

    # Área de um setor circular
    def area_setor_circular(raio, angulo):
        import math
        return (angulo / 360) * math.pi * raio**2

    # Área da superfície de um cilindro
    def area_superficie_cilindro(raio_base, altura):
        import math
        return 2 * math.pi * raio_base * (raio_base + altura)

    # Área da superfície de um cone
    def area_superficie_cone(raio_base, geratriz):
        import math
        return math.pi * raio_base * (raio_base + geratriz)

    # Comprimento de uma circunferência
    def comprimento_circunferencia(self, raio):
        import math
        return 2 * math.pi * raio

    # Raio da esfera circunscrita a um tetraedro regular
    def raio_esfera_circunscrita_tetraedro_regular(aresta):
        import math
        return (math.sqrt(6) / 4) * aresta

    # Raio da esfera circunscrita a um cubo
    def raio_esfera_circunscrita_cubo(aresta):
        import math
        return (math.sqrt(3) / 2) * aresta

    # Volume de um octaedro regular
    def volume_octaedro_regular(aresta):
        import math
        return (2/3) * math.sqrt(2) * aresta**3

    # Área da superfície de um octaedro regular
    def area_superficie_octaedro_regular(aresta):
        import math
        return 2 * math.sqrt(3) * aresta**2

    # Distância entre dois pontos no espaço 2D
    def distancia_pontos_2D(x1, y1, x2, y2):
        import math
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # Distância entre dois pontos no espaço 3D
    def distancia_pontos_3D(x1, y1, z1, x2, y2, z2):
        import math
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

    # Área de um triângulo no espaço 2D, dados os pontos (x1, y1), (x2, y2) e (x3, y3)
    def area_triangulo_2D( x1, y1, x2, y2, x3, y3):
        return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2)

    # Área de um triângulo no espaço 3D, dados os pontos (x1, y1, z1), (x2, y2, z2) e (x3, y3, z3)
    def area_triangulo_3D(x1, y1, z1, x2, y2, z2, x3, y3, z3):
        import math

        # Fórmula da distância entre dois pontos no espaço 3D
        def distancia_pontos_3D(x1, y1, z1, x2, y2, z2):
            return ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)**0.5

        a = distancia_pontos_3D(x1, y1, z1, x2, y2, z2)
        b = distancia_pontos_3D(x2, y2, z2, x3, y3, z3)
        c = distancia_pontos_3D(x1, y1, z1, x3, y3, z3)
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


    # Volume de um tetraedro no espaço 3D, dados os pontos (x1, y1, z1), (x2, y2, z2), (x3, y3, z3) e (x4, y4, z4)
    def volume_tetraedro_3D(x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4):
        import numpy as np
        matriz = np.array([[x1-x4, x2-x4, x3-x4], [y1-y4, y2-y4, y3-y4], [z1-z4, z2-z4, z3-z4]])
        return abs(np.linalg.det(matriz)) / 6

    # Distância de um ponto a um plano no espaço 3D, dados os coeficientes (a, b, c, d) do plano e as coordenadas (x, y, z) do ponto
    def distancia_ponto_plano_3D( a, b, c, d, x, y, z):
        import math
        return abs((a*x + b*y + c*z + d) / math.sqrt(a**2 + b**2 + c**2))

    # Equação da reta no espaço 3D, dados um ponto (x0, y0, z0) pertencente à reta e um vetor diretor (u, v, w) da reta
    def equacao_reta_3D(x0, y0, z0, u, v, w):
        return f"x = {x0} + {u}t, y = {y0} + {v}t, z = {z0} + {w}t"

    # Equação do plano no espaço 3D, dados os coeficientes (a, b, c, d) do plano
    def equacao_plano_3D(a, b, c, d):
        return f"{a}x + {b}y + {c}z + {d} = 0"

    # Vetor normal a um plano no espaço 3D, dados os coeficientes (a, b, c) do plano
    def vetor_normal_plano_3D( a, b, c):
        import numpy as np
        return np.array([a, b, c])

    # Ângulo entre dois planos no espaço 3D, dados os coeficientes (a1, b1, c1) e (a2, b2, c2) dos planos
    def angulo_entre_planos_3D(a1, b1, c1, a2, b2, c2):
        import math
        
        # Vetor normal ao primeiro plano
        vetor_normal1 = [a1, b1, c1]

        # Vetor normal ao segundo plano
        vetor_normal2 = [a2, b2, c2]

        # Produto escalar entre os vetores normais
        produto_escalar_vetores = sum(v1 * v2 for v1, v2 in zip(vetor_normal1, vetor_normal2))

        # Comprimento dos vetores normais
        norma_vetor1 = math.sqrt(sum(v ** 2 for v in vetor_normal1))
        norma_vetor2 = math.sqrt(sum(v ** 2 for v in vetor_normal2))

        # Cálculo do ângulo
        angulo_radianos = math.acos(produto_escalar_vetores / (norma_vetor1 * norma_vetor2))

        # Converter para graus
        angulo_graus = math.degrees(angulo_radianos)
        
        return angulo_graus

    

    def distancia_entre_planos_3D(a1, b1, c1, d1, a2, b2, c2, d2):
        import numpy as np
        # Vetor normal ao plano 1
        vetor_normal1 = np.array([a1, b1, c1])

        # Vetor normal ao plano 2
        vetor_normal2 = np.array([a2, b2, c2])

        # Distância entre os planos
        return np.abs(d2 - d1) / np.linalg.norm(np.cross(vetor_normal1, vetor_normal2))

    # Centro de massa de um conjunto de pontos no espaço 2D, dados os pontos como listas [x1, x2, ..., xn] e [y1, y2, ..., yn]
    def centro_massa_2D(pontos_x, pontos_y):
        num_pontos = len(pontos_x)
        soma_x = sum(pontos_x)
        soma_y = sum(pontos_y)
        return soma_x / num_pontos, soma_y / num_pontos

    # Centro de massa de um conjunto de pontos no espaço 3D, dados os pontos como listas [x1, x2, ..., xn], [y1, y2, ..., yn] e [z1, z2, ..., zn]
    def centro_massa_3D(pontos_x, pontos_y, pontos_z):
        num_pontos = len(pontos_x)
        soma_x = sum(pontos_x)
        soma_y = sum(pontos_y)
        soma_z = sum(pontos_z)
        return soma_x / num_pontos, soma_y / num_pontos, soma_z / num_pontos

    # Distância entre um ponto e uma curva no espaço 2D
    def distancia_ponto_curva_2D(x_ponto, y_ponto, curva):
        menor_distancia = float("inf")
        for i in range(len(curva) - 1):
            x1, y1 = curva[i]
            x2, y2 = curva[i + 1]

            # Fórmula da distância entre um ponto (x0, y0) e uma reta definida por dois pontos (x1, y1) e (x2, y2)
            a = y2 - y1
            b = x1 - x2
            c = x2 * y1 - x1 * y2
            distancia = abs(a * x_ponto + b * y_ponto + c) / ((a**2 + b**2)**0.5)

            if distancia < menor_distancia:
                menor_distancia = distancia

        return menor_distancia


    # Distância entre um ponto e um segmento de reta no espaço 2D
    def distancia_ponto_segmento_2D(x_ponto, y_ponto, x1, y1, x2, y2):
        try:
            # Fórmula da distância entre dois pontos no espaço 2D
            def distancia_pontos_2D(x1, y1, x2, y2):
                return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

            produto_escalar_p1 = (x_ponto - x1) * (x2 - x1) + (y_ponto - y1) * (y2 - y1)
            produto_escalar_p2 = (x_ponto - x2) * (x1 - x2) + (y_ponto - y2) * (y1 - y2)

            if produto_escalar_p1 <= 0:
                return distancia_pontos_2D(x_ponto, y_ponto, x1, y1)
            elif produto_escalar_p2 <= 0:
                return distancia_pontos_2D(x_ponto, y_ponto, x2, y2)
            else:
                # Fórmula da área de um triângulo no espaço 2D
                def area_triangulo_2D(x1, y1, x2, y2, x3, y3):
                    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)

                area_triangulo = area_triangulo_2D(x_ponto, y_ponto, x1, y1, x2, y2)
                base = distancia_pontos_2D(x1, y1, x2, y2)
                return 2 * area_triangulo / base
        except Exception as e:
            return e


    # Círculo circunscrito a um triângulo no espaço 2D, dados os pontos (x1, y1), (x2, y2) e (x3, y3)
    def circulo_circunscrito_triangulo_2D(x1, y1, x2, y2, x3, y3):
        try:
            import math

            # Fórmula da distância entre dois pontos no espaço 2D
            def distancia_pontos_2D(x1, y1, x2, y2):
                return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

            a = distancia_pontos_2D(x2, y2, x3, y3)
            b = distancia_pontos_2D(x1, y1, x3, y3)
            c = distancia_pontos_2D(x1, y1, x2, y2)
            s = (a + b + c) / 2
            raio = (a * b * c) / (4 * math.sqrt(s * (s - a) * (s - b) * (s - c)))
            centro_x = ((x1 * b * c) + (x2 * a * c) + (x3 * a * b)) / (a + b + c)
            centro_y = ((y1 * b * c) + (y2 * a * c) + (y3 * a * b)) / (a + b + c)
            return centro_x, centro_y, raio
        except Exception as e:
            return e


    # Elipse circunscrita a um quadrilátero convexo no espaço 2D, dados os pontos (x1, y1), (x2, y2), (x3, y3) e (x4, y4)
    def elipse_circunscrita_quadrilatero_2D(x1, y1, x2, y2, x3, y3, x4, y4):
        try:
            import math

            # Fórmula da distância entre dois pontos no espaço 2D
            def distancia_pontos_2D(x1, y1, x2, y2):
                return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

            centro_x = (x1 + x2 + x3 + x4) / 4
            centro_y = (y1 + y2 + y3 + y4) / 4
            a = distancia_pontos_2D(centro_x, centro_y, x1, y1)
            b = distancia_pontos_2D(centro_x, centro_y, x2, y2)
            c = distancia_pontos_2D(centro_x, centro_y, x3, y3)
            d = distancia_pontos_2D(centro_x, centro_y, x4, y4)
            semi_eixo_menor = (a + b + c + d) / 4
            semi_eixo_maior = math.sqrt((a**2 + b**2 + c**2 + d**2) / 4)
            return centro_x, centro_y, semi_eixo_maior, semi_eixo_menor
        except Exception as e:
            return e


    # Soma de dois vetores no espaço 2D
    def soma_vetores_2D(vetor1, vetor2):
        try:
            return [vetor1[0] + vetor2[0], vetor1[1] + vetor2[1]]
        except Exception as e:
            return e

    # Subtração de dois vetores no espaço 2D
    def subtracao_vetores_2D(vetor1, vetor2):
        try:
            return [vetor1[0] - vetor2[0], vetor1[1] - vetor2[1]]
        except Exception as e:
            return e

    # Produto escalar entre dois vetores no espaço 2D
    def produto_escalar_vetores_2D(self, x1, y1, x2, y2):
        try:
            return x1 * x2 + y1 * y2
        except Exception as e:
            return e

    # Verifica se dois vetores são paralelos no espaço 2D
    def sao_paralelos_2D(vetor1, vetor2):
        try:
            return abs(vetor1[0] * vetor2[1] - vetor1[1] * vetor2[0]) < 1e-10
        except Exception as e:
            return e

    # Verifica se dois vetores são ortogonais no espaço 2D
    def sao_ortogonais_2D(vetor1, vetor2):
        try:
            return abs(vetor1[0] * vetor2[0] + vetor1[1] * vetor2[1]) < 1e-10
        except Exception as e:
            return e

    # Verifica se três pontos são colineares no espaço 2D, dados os pontos (x1, y1), (x2, y2) e (x3, y3)
    def sao_colineares_2D(x1, y1, x2, y2, x3, y3):
        try:
            return abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) < 1e-10
        except Exception as e:
            return e

    # Verifica se quatro pontos formam um quadrilátero convexo no espaço 2D, dados os pontos (x1, y1), (x2, y2), (x3, y3) e (x4, y4)
    def formam_quadrilatero_convexo_2D(x1, y1, x2, y2, x3, y3, x4, y4):
        try:
            a1 = (x2 - x1) * (y4 - y1) - (x4 - x1) * (y2 - y1)
            a2 = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
            a3 = (x4 - x3) * (y2 - y3) - (x2 - x3) * (y4 - y3)
            a4 = (x4 - x3) * (y1 - y3) - (x1 - x3) * (y4 - y3)
            return (a1 * a3 < 0) and (a2 * a4 < 0)
        except Exception as e:
            return e

    def comprimento_vetor_3D(self,vetor):
        try:
            import math
            return math.sqrt(vetor[0]**2 + vetor[1]**2 + vetor[2]**2)
        except Exception as e:
            return e

    def produto_escalar(self, vetor1, vetor2):
        try:
            return vetor1[0] * vetor2[0] + vetor1[1] * vetor2[1] + vetor1[2] * vetor2[2]
        except Exception as e:
            return e

    def area_poligono_convexo(vertices):
        try:
            n = len(vertices)
            area = 0.0
            for i in range(n):
                j = (i + 1) % n
                area += vertices[i][0] * vertices[j][1]
                area -= vertices[j][0] * vertices[i][1]
            return 0.5 * abs(area)
        except Exception as e:
            return e
    
    def area_poligono(vertices):
        try:
            n = len(vertices)
            area = 0.0
            for i in range(n):
                j = (i + 1) % n
                area += vertices[i][0] * vertices[j][1]
                area -= vertices[j][0] * vertices[i][1]
            return 0.5 * abs(area)
        except Exception as e:
            return e
    
    def circunferencia_circunscrita(triangulo):
        try:
            import math
            import numpy as np
            A, B, C = triangulo
            a = np.linalg.norm(B - C)
            b = np.linalg.norm(C - A)
            c = np.linalg.norm(A - B)
            s = (a + b + c) / 2.0
            raio = (a * b * c) / (4.0 * math.sqrt(s * (s - a) * (s - b) * (s - c)))
            centro = (a**2 * (b**2 + c**2 - a**2) * A + b**2 * (c**2 + a**2 - b**2) * B + c**2 * (a**2 + b**2 - c**2) * C) / (a**2 * (b**2 + c**2 - a**2) + b**2 * (c**2 + a**2 - b**2) + c**2 * (a**2 + b**2 - c**2))
            return (centro, raio)
        except Exception as e:
            return e

    
    def equacao_circunferencia(ponto1, ponto2, ponto3):
        try:
            import numpy as np
            x1, y1 = ponto1
            x2, y2 = ponto2
            x3, y3 = ponto3
            A = np.array([[x1, y1, 1], [x2, y2, 1], [x3, y3, 1]])
            b = np.array([[-(x1**2 + y1**2)], [-(x2**2 + y2**2)], [-(x3**2 + y3**2)]])
            a, b, c = np.linalg.solve(A, b)
            return a[0], b[0], c[0]
        except Exception as e:
            return e
    
    def calcular_euler(v=None, f=None, a=None):
        try:
            if sum(val is not None for val in [v, f, a]) != 2:
                raise ValueError("Apenas dois dos valores V, F e A devem ser fornecidos.")

            if v is None:
                v = a + 2 - f
            elif f is None:
                f = a + 2 - v
            elif a is None:
                a = v + f - 2

            return f"Vertices:{v}, Faces:{f}, Arestas:{a}"
        except Exception as e:
            return e


#Classe de Criptografia
class Criptografia:
    # Cifra de César (criptografar)
    def cifra_cesar_encrypt( texto, chave):
        try:
            texto_cifrado = ""
            for char in texto:
                if char.isalpha():
                    base = ord('a') if char.islower() else ord('A')
                    char_cifrado = chr((ord(char) - base + chave) % 26 + base)
                    texto_cifrado += char_cifrado
                else:
                    texto_cifrado += char
            return texto_cifrado
        except Exception as e:
            return e

    # Cifra de César (descriptografar)
    def cifra_cesar_decrypt(texto_cifrado, chave):
        try:
            texto_original = ""
            for char in texto_cifrado:
                if char.isalpha():
                    base = ord('a') if char.islower() else ord('A')
                    char_original = chr((ord(char) - base - chave) % 26 + base)
                    texto_original += char_original
                else:
                    texto_original += char
            return texto_original
        except Exception as e:
            return e

    # Cifra de Substituição (criptografar)
    def cifra_substituicao_encrypt( texto, chave):
        try:
            alfabeto = "abcdefghijklmnopqrstuvwxyz"
            texto_cifrado = ""
            for char in texto:
                if char.isalpha():
                    index = alfabeto.index(char.lower())
                    char_cifrado = chave[index].upper() if char.isupper() else chave[index]
                    texto_cifrado += char_cifrado
                else:
                    texto_cifrado += char
            return texto_cifrado
        except Exception as e:
            return e

    # Cifra de Substituição (descriptografar)
    def cifra_substituicao_decrypt(texto_cifrado, chave):
        try:
            alfabeto = "abcdefghijklmnopqrstuvwxyz"
            texto_original = ""
            for char in texto_cifrado:
                if char.isalpha():
                    if char.islower():
                        index = chave.find(char)
                        char_original = alfabeto[index]
                        texto_original += char_original
                    else:
                        index = chave.find(char.lower())
                        char_original = alfabeto[index].upper()
                        texto_original += char_original
                else:
                    texto_original += char
            return texto_original
        except Exception as e:
            return e

    # Cifra de Vigenère (criptografar)
    def cifra_vigenere_encrypt(texto, chave):
        try:
            alfabeto = "abcdefghijklmnopqrstuvwxyz"
            texto_cifrado = ""
            chave_repetida = "".join(chave[i % len(chave)] for i in range(len(texto)))
            for i in range(len(texto)):
                char = texto[i]
                if char.isalpha():
                    base = ord('a') if char.islower() else ord('A')
                    index_texto = alfabeto.index(char.lower())
                    index_chave = alfabeto.index(chave_repetida[i].lower())
                    char_cifrado = chr((index_texto + index_chave) % 26 + base)
                    texto_cifrado += char_cifrado
                else:
                    texto_cifrado += char
            return texto_cifrado
        except Exception as e:
            return e

    # Cifra de Vigenère (descriptografar)
    def cifra_vigenere_decrypt(texto_cifrado, chave):
        try:
            alfabeto = "abcdefghijklmnopqrstuvwxyz"
            chave_repetida = "".join(chave[i % len(chave)] for i in range(len(texto_cifrado)))
            texto_decifrado = ""
            for i in range(len(texto_cifrado)):
                char = texto_cifrado[i]
                if char.isalpha():
                    base = ord('a') if char.islower() else ord('A')
                    index_texto = alfabeto.index(char.lower())
                    index_chave = alfabeto.index(chave_repetida[i].lower())
                    char_decifrado = chr((index_texto - index_chave) % 26 + base)
                    texto_decifrado += char_decifrado
                else:
                    texto_decifrado += char
            return texto_decifrado
        except Exception as e:
            return e 

    # Cifra de Vernam (XOR one-time pad)
    def cifra_vernam_encrypt(texto, chave):
        try:
            texto_cifrado = ""
            for i in range(len(texto)):
                char = texto[i]
                if char.isalpha():
                    char_cifrado = chr(ord(char) ^ ord(chave[i]))
                    texto_cifrado += char_cifrado
                else:
                    texto_cifrado += char
            return texto_cifrado
        except Exception as e:
            return e

    # Algoritmo de Transposição (criptografar)
    def transposicao_encrypt(texto, chave):
        try:
            tamanho_chave = len(chave)
            colunas = {chave[i]: texto[i : i + tamanho_chave] for i in range(0, len(texto), tamanho_chave)}
            texto_cifrado = "".join(colunas[chave[i]] for i in sorted(range(tamanho_chave), key=lambda k: chave[k]))
            return texto_cifrado
        except Exception as e:
            return e

    # Algoritmo de Transposição (descriptografar)
    def transposicao_decrypt(texto_cifrado, chave):
        try:
            tamanho_chave = len(chave)
            num_colunas = len(texto_cifrado) // tamanho_chave
            colunas = [texto_cifrado[i : i + num_colunas] for i in range(0, len(texto_cifrado), num_colunas)]
            texto_decifrado = "".join(colunas[chave.index(letra)] for letra in sorted(chave))
            return texto_decifrado
        except Exception as e:
            return e
        
        

    def verificar_senha_hackeada(senha):
        import requests
        import hashlib
        hash_senha = hashlib.sha1(senha.encode('utf-8')).hexdigest().upper()
        prefixo_hash, sufixo_hash = hash_senha[:5], hash_senha[5:]
        url = f'https://api.pwnedpasswords.com/range/{prefixo_hash}'
        resposta = requests.get(url)
        senhas_vazadas = (linha.split(':') for linha in resposta.text.splitlines())
        for sufixo, contagem in senhas_vazadas:
            if sufixo_hash == sufixo:
                return int(contagem)
        return 0
    
        

    def verificar_email_comprometido(email):
        import requests
        import hashlib
        hash_email = hashlib.sha1(email.encode('utf-8')).hexdigest().upper()
        prefixo_hash, sufixo_hash = hash_email[:5], hash_email[5:]
        url = f'https://haveibeenpwned.com/api/v3/breachedaccount/{prefixo_hash}'
        cabecalhos = {'User-Agent': 'Verificador-de-email-v1'}
        resposta = requests.get(url, headers=cabecalhos)
        
        if resposta.status_code == 200:
            # Se o e-mail foi encontrado em um banco de dados vazado
            dados_vazados = resposta.json()
            sites_comprometidos = [dados['Name'] for dados in dados_vazados]
            return True, sites_comprometidos
        elif resposta.status_code == 404:
            # Se o e-mail não foi encontrado em nenhum banco de dados vazado
            return 0
        else:
            # Algum erro ocorreu na solicitação à API
            print(f"Erro na solicitação à API: {resposta.status_code} - {resposta.text}")
            return None, []
        
        
    def calcular_hash_sha256(dados):
        import hashlib
        hash_obj = hashlib.sha256()
        hash_obj.update(dados.encode('utf-8'))
        return hash_obj.hexdigest()
    
    def calcular_hash_sha224(dados):
        import hashlib
        hash_obj = hashlib.sha224()
        hash_obj.update(dados.encode('utf-8'))
        return hash_obj.hexdigest()
    
    def calcular_hash_sha384(dados):
        import hashlib
        hash_obj = hashlib.sha384()
        hash_obj.update(dados.encode('utf-8'))
        return hash_obj.hexdigest()
    
    def calcular_hash_sha1(dados):
        import hashlib
        hash_obj = hashlib.sha1()
        hash_obj.update(dados.encode('utf-8'))
        return hash_obj.hexdigest()
    


    def criptografar_mensagem_(mensagem, senha):
        import os
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
        from cryptography.hazmat.primitives import padding
        from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
        from cryptography.hazmat.backends import default_backend

        # Gerar uma chave secreta a partir da senha usando PBKDF2HMAC
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        chave_secreta = kdf.derive(senha.encode('utf-8'))

        # Criar um vetor de inicialização (IV) aleatório
        iv = os.urandom(16)

        # Criar um objeto Cipher AES em modo CBC
        cipher = Cipher(algorithms.AES(chave_secreta), modes.CBC(iv), backend=default_backend())

        # Criptografar a mensagem
        padder = padding.PKCS7(128).padder()
        mensagem_pad = padder.update(mensagem.encode('utf-8')) + padder.finalize()
        encryptor = cipher.encryptor()
        mensagem_cifrada = encryptor.update(mensagem_pad) + encryptor.finalize()

        # Retornar o resultado como uma tupla contendo o IV, o salt e a mensagem cifrada
        return iv, salt, mensagem_cifrada
    

    def descriptografar_mensagem_(iv, salt, mensagem_cifrada, senha):
        import os
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
        from cryptography.hazmat.primitives import padding
        from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
        from cryptography.hazmat.backends import default_backend

        # Gerar a chave secreta a partir da senha e do salt usando PBKDF2HMAC
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        chave_secreta = kdf.derive(senha.encode('utf-8'))

        # Criar um objeto Cipher AES em modo CBC
        cipher = Cipher(algorithms.AES(chave_secreta), modes.CBC(iv), backend=default_backend())

        # Descriptografar a mensagem
        decryptor = cipher.decryptor()
        mensagem_pad = decryptor.update(mensagem_cifrada) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        mensagem_original = unpadder.update(mensagem_pad) + unpadder.finalize()

        # Retornar a mensagem original
        return mensagem_original.decode('utf-8')
    

   
    def gerar_senha_extremamente_forte(tamanho=20):
        import string, secrets

        
        puc = "ӔӖӘӚӗ₱ӝӷ₰Ỏề₲№₽₡₴ợ₲忢忛忌徣徕徥怶怤飆飃颩颦颷飯驁騦驁騎馌ÑËùÜBõѢњѝẂﬄ€∏∑ẬẾĄĆ¶\⿊はばぱねなに㏂㏈㏃㏉㍞㍡㍝㍬㎒丗㸿ｲｳｴｵ￦ｶｸϖϗϘϙϚϛϜϝϞϟϠϡϢϣϤϥϦϧϨϩϪϫϬϭϮϯϰϱϲϳϴϵ϶∥∎∄∑∇∏⏈⌫⌭⌯⌱✬⛞⛴⛄✈✓✈⛱⛹✉✤⛬✮✏✪✱✭✱✠♪♬♼⚪⛁⡘⢅⢾⢸⣃⨪⧖⧎⨣⨝⨖⧯⧮⧈▓␀␂␌␛␕␑␎⑈⇜⇪↣⇛ǰǱǷΏΉΐẋὥἹἴὒἯỮὪЩѣѢồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦ®±¤¢ŁĎĘæœǺŋĝĿłƒžŦέζπЮ‗џњљЉ◄♣ﬂ♫╬∫⅛ﬂ⅝⅞║≠≡◊"
        
          
        caracteres = string.ascii_letters + string.digits + string.punctuation + puc
        senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))

        if tamanho <= -20:
            tamanho = tamanho * (-1)

        elif tamanho < 20:
            return "Não pode ser uma senha menos que 20 carateres"
        
        # Verifica se a senha gerada contém pelo menos um caractere de cada categoria
        while not (any(c in string.ascii_lowercase for c in senha) and
                any(c in string.ascii_uppercase for c in senha) and
                any(c in string.digits for c in senha) and
                any(c in string.punctuation for c in senha) and
                any(c in puc for c in senha)):
            senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))

        return senha
    

    def gerar_senha_extremamente_forte__amdr(tamanho:int):
        import string, secrets
        with open("simbolo.txt", 'r', encoding='utf-8') as puc:
            puc = puc.read()
        caracteres = string.ascii_letters + string.digits + string.punctuation + puc
        senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
        if tamanho <= 3:
            raise "Não pode ser uma senha com quantidade de caratere(s) menos ou igual a 3"
        else:
            # Verifica se a senha gerada contém pelo menos um caractere de cada categoria
            while not (any(c in string.ascii_lowercase for c in senha) and
                    any(c in string.ascii_uppercase for c in senha) and
                    any(c in string.digits for c in senha) and
                    any(c in string.punctuation for c in senha) and
                    any(c in puc for c in senha)):
                senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))

            return senha
    

    
    def gerar_token_autenticacao(n:int):
        import secrets
        # Defina o tamanho do token em bytes (recomendado usar pelo menos 32 bytes para segurança adequada)
        tamanho_token = n

        # Gerar o token hexadecimal seguro
        token = secrets.token_hex(tamanho_token)

        return token
    
    def gerar_codigo_totp_ch(chave_secreta):
        import pyotp
        # Criar um objeto TOTP com a chave secreta fornecida
        totp = pyotp.TOTP(chave_secreta)

        # Gerar o código TOTP de 4 dígitos
        codigo = totp.now()

        return codigo
    
    def gerar_codigo_totp_qr_cd(caminho_imagem_qr_code):
        try:
            import pyotp, cv2

            def extrair_chave_secreta(url_otp):
                import re, pyotp
                padrao = r'secret=([A-Z0-9]+)'
                chave_secreta = re.search(padrao, url_otp)
                if chave_secreta:
                    totp = pyotp.TOTP(chave_secreta.group(1))  # Utilize chave_secreta.group(1) para obter o valor da chave
                    codigo = totp.now()  # Gerar o código TOTP de 6 dígitos
                    return codigo
                else:
                    return None

            image = cv2.imread(caminho_imagem_qr_code)
            detector = cv2.QRCodeDetector()
            retval, decoded_info, points, straight_qrcode = detector.detectAndDecodeMulti(image)

            if retval:
                codigo_totp = extrair_chave_secreta(decoded_info[0])
                return f"{decoded_info[0]}\ncodigo totp: {codigo_totp}"
            else:
                return None

        except:
            raise Exception("Não Consigo abrir a imagem, Verifique o Nome de novo")


    def converter_hex_para_base32(hex_key):
        import base64
        # Verificar se a chave em formato hexadecimal é válida
        if hex_key is None or not isinstance(hex_key, str):
            raise ValueError("Chave em formato hexadecimal inválida.")

        # Decodificar a chave hexadecimal para bytes
        key_bytes = bytes.fromhex(hex_key)

        # Codificar os bytes para base32
        base32_key = base64.b32encode(key_bytes).decode()

        return base32_key


#Classe de Analise Combinatória
class Analise_Combinatoria:
    

    # Arranjo simples (Permutação)
    def arranjo(n:int, k:int):
        import math
        return math.factorial(n) // math.factorial(n - k)

    # Combinação (Binômio)
    def combinacao(n:int, k:int):
        import math
        return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

    # Combinação com repetição
    def combinacao_repeticao(n:int, k:int):
        import math
        def combinacao(n, k):
            return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
        return combinacao(n + k - 1, k)

    # Permutação com repetição
    def permutacao_repeticao(lista):
        import math
        divisor = 1
        for elem in set(lista):
            divisor *= math.factorial(lista.count(elem))
        return math.factorial(len(lista)) // divisor

    # Permutação circular
    def permutacao_circular(n:int):
        import math
        return math.factorial(n - 1)

    # Números de Stirling de segunda espécie
    def numeros_stirling_segunda(n, k):
        import numpy as np
        if n == k == 0:
            return 1
        elif n == 0 or k == 0:
            return 0
        else:
            s = np.zeros((n + 1, k + 1))
            s[0][0] = 1
            for i in range(1, n + 1):
                for j in range(1, k + 1):
                    s[i][j] = j * s[i - 1][j] + s[i - 1][j - 1]
            return s[n][k]

    # Números de Stirling de primeira espécie
    def numeros_stirling_primeira(n, k):
        import numbers as np
        if n == k == 0:
            return 1
        elif n == 0 or k == 0:
            return 0
        else:
            s = np.zeros((n + 1, k + 1))
            s[0][0] = 1
            for i in range(1, n + 1):
                for j in range(1, k + 1):
                    s[i][j] = (i - 1) * s[i - 1][j] + s[i - 1][j - 1]
            return s[n][k]
    
    # Coeficiente multinomial
    def multinomial(*args):
        import math
        numerator = math.factorial(sum(args))
        denominator = 1
        for arg in args:
            denominator *= math.factorial(arg)
        return numerator // denominator

    # Número de Bell
    def numero_bell(n):
        bell = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        bell[0][0] = 1

        for i in range(1, n + 1):
            bell[i][0] = bell[i - 1][i - 1]
            for j in range(1, i + 1):
                bell[i][j] = bell[i - 1][j - 1] + bell[i][j - 1]

        return bell[n][0]

    # Número de derivações
    def numero_derivacoes(n):
        from sympy import binomial
        return sum((-1)**k * binomial(n, k) * (n - k)**n for k in range(n + 1))


    # Coeficiente binomial generalizado
    def coeficiente_binomial_generalizado(n, k, m):
        import math
        return math.factorial(n) // (math.factorial(k) * math.factorial(m) * math.factorial(n - k - m))

    # Número de derangements
    def numero_derangement_biblioteca(n):
        import math
        return math.factorial(n) * sum((-1)**i / math.factorial(i) for i in range(n + 1))


    # Triângulo de Pascal
    def triangulo_pascal(n:int):
        pascal = [[1]]
        for i in range(1, n + 1):
            linha = [1]
            for j in range(1, i):
                linha.append(pascal[i - 1][j - 1] + pascal[i - 1][j])
            linha.append(1)
            pascal.append(linha)
        return pascal

    # Números harmônicos
    def numeros_harmonicos(n):
        return sum([1/i for i in range(1, n + 1)])

    # Número de Fibonacci
    def fibonacci(n):
        from sympy import fibonacci
        return fibonacci(n)

    # Número de Lucas
    def lucas(n):
        from sympy import lucas
        return lucas(n)

    # Números de Catalão
    def numeros_catalao(n):
        from sympy import catalan
        return catalan(n)

    # Sequência de Farey
    def sequencia_farey(n):
        farey = set()
        for denominator in range(1, n + 1):
            for numerator in range(denominator + 1):
                farey.add(numerator / denominator)
        return sorted(list(farey))

    # Número de Partições
    

    def numero_particoes(n):
        from sympy import partition
        return partition(n)


    # Número de Stirling de segunda espécie (versão iterativa)
    def numeros_stirling_segunda_iterativo(n, k):
        if n == k == 0:
            return 1
        elif n == 0 or k == 0:
            return 0

        stirling = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            stirling[i][0] = 0
        for i in range(k + 1):
            stirling[0][i] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                if i == j:
                    stirling[i][j] = 1
                else:
                    stirling[i][j] = j * stirling[i - 1][j] + stirling[i - 1][j - 1]

        return stirling[n][k]

    # Número de Stirling de primeira espécie (versão iterativa)
    def numeros_stirling_primeira_iterativo(n, k):
        if n == k == 0:
            return 1
        elif n == 0 or k == 0:
            return 0

        stirling = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            stirling[i][0] = 0
        for i in range(k + 1):
            stirling[0][i] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                if i == j:
                    stirling[i][j] = 1
                else:
                    stirling[i][j] = (i - 1) * stirling[i - 1][j] + stirling[i - 1][j - 1]

        return stirling[n][k]

    # Coeficiente multinomial (versão iterativa)
    def multinomial_iterativo(*args):
        import math
        n = sum(args)
        numerator = 1
        for i in range(n, n - sum(args), -1):
            numerator *= i
        denominator = math.prod([math.factorial(arg) for arg in args])
        return numerator // denominator

    # Número de Bell (versão iterativa)
    def numero_bell_iterativo(n):
        bell = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        bell[0][0] = 1

        for i in range(1, n + 1):
            bell[i][0] = bell[i - 1][i - 1]
            for j in range(1, i + 1):
                bell[i][j] = bell[i - 1][j - 1] + bell[i][j - 1]

        return bell[n][0]

    

    # Número de derivações
    def numero_derivacoes(n):
        import scipy.special as sp
        return sum([(-1)**k * sp.comb(n, k) * (n - k)**n for k in range(n + 1)])

    # Coeficiente binomial generalizado (versão iterativa)
    def coeficiente_binomial_generalizado_iterativo(n, k, m):
        import math
        numerator = 1
        for i in range(n, n - k, -1):
            numerator *= i
        denominator = math.prod([math.factorial(arg) for arg in [k, m, n - k - m]])
        return numerator // denominator

    # Número de derangements (versão iterativa)
    def numero_derangement_iterativo(n):
        if n == 0:
            return 1
        elif n == 1:
            return 0

        derangement = [0] * (n + 1)
        derangement[0], derangement[1] = 1, 0

        for i in range(2, n + 1):
            derangement[i] = (i - 1) * (derangement[i - 1] + derangement[i - 2])

        return derangement[n]

    # Números harmônicos (versão iterativa)
    def numeros_harmonicos_iterativo(n):
        return sum([1/i for i in range(1, n + 1)])

    # Número de Fibonacci (versão iterativa)
    def fibonacci_iterativo(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1

        fib = [0] * (n + 1)
        fib[1] = 1

        for i in range(2, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]

        return fib[n]

    # Número de Lucas (versão iterativa)
    def lucas_iterativo(n):
        if n == 0:
            return 2
        elif n == 1:
            return 1

        lucas = [0] * (n + 1)
        lucas[1] = 1
        lucas[2] = 2

        for i in range(3, n + 1):
            lucas[i] = lucas[i - 1] + lucas[i - 2]

        return lucas[n]

    # Números de Catalão (versão iterativa)
    def numeros_catalao_iterativo(n):
        catalan = [0] * (n + 1)
        catalan[0] = 1

        for i in range(1, n + 1):
            for j in range(i):
                catalan[i] += catalan[j] * catalan[i - j - 1]

        return catalan[n]

    # Sequência de Farey (versão iterativa)
    def sequencia_farey_iterativo(n):
        farey = set()
        for denominator in range(1, n + 1):
            for numerator in range(1, denominator + 1):
                farey.add(numerator / denominator)
        return sorted(list(farey))

    # Número de Partições (versão iterativa)
    def numero_particoes_iterativo(n, m):
        partitions = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            partitions[i][0] = 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if j >= i:
                    partitions[i][j] = partitions[i - 1][j] + partitions[i][j - i]
                else:
                    partitions[i][j] = partitions[i - 1][j]

        return partitions[n][m]


#Classe de Probabilidade
class Probabilidade:
    # Probabilidade de um evento simples
    @staticmethod
    def probabilidade_evento_simples(evento_favoravel, espaco_amostral):
        return evento_favoravel / espaco_amostral

    # Probabilidade complementar
    @staticmethod
    def probabilidade_complementar(probabilidade_evento):
        return 1 - probabilidade_evento

    # Probabilidade conjunta (Eventos independentes)
    @staticmethod
    def probabilidade_conjunta_independentes(probabilidade_evento1, probabilidade_evento2):
        return probabilidade_evento1 * probabilidade_evento2

    # Probabilidade conjunta (Eventos dependentes)
    @staticmethod
    def probabilidade_conjunta_dependentes(probabilidade_evento1, probabilidade_evento2_dado_evento1):
        return probabilidade_evento1 * probabilidade_evento2_dado_evento1

    # Probabilidade da união de eventos mutuamente exclusivos
    @staticmethod
    def probabilidade_uniao_mutuamente_exclusivos(probabilidade_evento1, probabilidade_evento2):
        return probabilidade_evento1 + probabilidade_evento2

    # Probabilidade da união de eventos não mutuamente exclusivos
    @staticmethod
    def probabilidade_uniao_nao_mutuamente_exclusivos(probabilidade_evento1, probabilidade_evento2, probabilidade_intersecao):
        return probabilidade_evento1 + probabilidade_evento2 - probabilidade_intersecao

    # Probabilidade condicional
    @staticmethod
    def probabilidade_condicional(probabilidade_evento1, probabilidade_evento2_dado_evento1):
        return probabilidade_evento2_dado_evento1 / probabilidade_evento1

    # Teorema de Bayes
    @staticmethod
    def teorema_bayes(probabilidade_evento1, probabilidade_evento2_dado_evento1, probabilidade_evento2):
        return (probabilidade_evento2_dado_evento1 * probabilidade_evento1) / probabilidade_evento2

    # Probabilidade de interseção de eventos independentes
    @staticmethod
    def probabilidade_intersecao_independentes(probabilidade_evento1, probabilidade_evento2):
        return probabilidade_evento1 * probabilidade_evento2

    # Probabilidade de interseção de eventos dependentes
    @staticmethod
    def probabilidade_intersecao_dependentes(probabilidade_evento1, probabilidade_evento2_dado_evento1):
        return probabilidade_evento1 * probabilidade_evento2_dado_evento1

    # Regra da multiplicação (Eventos independentes)
    @staticmethod
    def regra_multiplicacao_independentes(probabilidade_eventos):
        from sympy import S, factorial, sqrt, prod, partition, integrate
        return prod(probabilidade_eventos)

    # Regra da multiplicação (Eventos dependentes)
    @staticmethod
    def regra_multiplicacao_dependentes(probabilidade_eventos_dado_evento_anterior):
        from sympy import S, factorial, sqrt, prod, partition, integrate
        return prod(probabilidade_eventos_dado_evento_anterior)

    # Probabilidade condicional múltipla
    @staticmethod
    def probabilidade_condicional_multipla(probabilidade_eventos):
        return probabilidade_eventos[-1] / probabilidade_eventos[:-1]

    # Probabilidade de um evento composto
    @staticmethod
    def probabilidade_evento_composto(probabilidades_eventos):
        return sum(probabilidades_eventos)

    # Probabilidade conjunta de eventos compostos independentes
    @staticmethod
    def probabilidade_conjunta_compostos_independentes(probabilidades_eventos):
        from sympy import S, factorial, sqrt, prod, partition, integrate
        return prod(probabilidades_eventos)

    # Probabilidade conjunta de eventos compostos dependentes
    @staticmethod
    def probabilidade_conjunta_compostos_dependentes(probabilidades_eventos_dado_evento_anterior):
        from sympy import S, factorial, sqrt, prod, partition, integrate
        return prod(probabilidades_eventos_dado_evento_anterior)

    # Probabilidade de eventos independentes não mutuamente exclusivos
    @staticmethod
    def probabilidade_independentes_nao_mutuamente_exclusivos(probabilidades_eventos):
        return sum(probabilidades_eventos) - sum(Probabilidade.probabilidade_intersecao_independentes(probabilidades_eventos))

    # Probabilidade de eventos dependentes não mutuamente exclusivos
    @staticmethod
    def probabilidade_dependentes_nao_mutuamente_exclusivos(probabilidades_eventos_dado_evento_anterior):
        return sum(probabilidades_eventos_dado_evento_anterior) - sum(Probabilidade.probabilidade_intersecao_dependentes(probabilidades_eventos_dado_evento_anterior))

    # Probabilidade de pelo menos um evento ocorrer
    @staticmethod
    def probabilidade_pelo_menos_um_evento(probabilidades_eventos):
        return Probabilidade.probabilidade_evento_composto(probabilidades_eventos) - Probabilidade.probabilidade_nenhum_evento_ocorrer(probabilidades_eventos)

    # Probabilidade de nenhum evento ocorrer
    @staticmethod
    def probabilidade_nenhum_evento_ocorrer(probabilidades_eventos):
        return 1 - Probabilidade.probabilidade_evento_composto(probabilidades_eventos)

    # Probabilidade de uma variável aleatória contínua (densidade de probabilidade)
    @staticmethod
    def densidade_probabilidade_variavel_aleatoria_contínua(x, f_x):
        return f_x(x)

    # Probabilidade de uma variável aleatória discreta
    @staticmethod
    def probabilidade_variavel_aleatoria_discreta(X, P_X):
        return sum([P_X[i] for i in X])

    # Esperança matemática de uma variável aleatória discreta
    @staticmethod
    def esperanca_variavel_aleatoria_discreta(X, P_X):
        return sum([x * P_X[i] for i, x in enumerate(X)])

    # Variância de uma variável aleatória discreta
    @staticmethod
    def variancia_variavel_aleatoria_discreta(X, P_X):
        esperanca = Probabilidade.esperanca_variavel_aleatoria_discreta(X, P_X)
        return sum([(x - esperanca)**2 * P_X[i] for i, x in enumerate(X)])

    # Desvio padrão de uma variável aleatória discreta
    @staticmethod
    def desvio_padrao_variavel_aleatoria_discreta(X, P_X):
        import math
        return math.sqrt(Probabilidade.variancia_variavel_aleatoria_discreta(X, P_X))

    # Esperança matemática de uma variável aleatória contínua
    @staticmethod
    def esperanca_variavel_aleatoria_continua(f_x, a, b):
        from sympy import integrate, symbols
        x = symbols('x')
        return integrate(x * f_x, (x, a, b))

    # Variância de uma variável aleatória contínua
    @staticmethod
    def variancia_variavel_aleatoria_continua(f_x, a, b):
        from sympy import integrate, symbols
        x = symbols('x')
        esperanca = Probabilidade.esperanca_variavel_aleatoria_continua(f_x, a, b)
        return integrate((x - esperanca)**2 * f_x, (x, a, b))

    # Desvio padrão de uma variável aleatória contínua
    @staticmethod
    def desvio_padrao_variavel_aleatoria_continua(f_x, a, b):
        from sympy import S, factorial, sqrt, prod, partition, integrate
        return sqrt(Probabilidade.variancia_variavel_aleatoria_continua(f_x, a, b))

