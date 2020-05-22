from .models import Registro, Cuidacoches, MonederoCuidacoches, Conductor, MonederoConductor, Relacion
from .forms import ValidacionCuidacoches, RegistroCuidacochesApp, ConductorForm, LoginForm, OcuparForm, LiberarForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout


def portada(request):
    return render(request, 'portada.html')


def register(request):
    if "usuario_type" in request.session:

        if request.session["usuario_type"] == 'conductor':
            return redirect('/home_conductor/')
        
        elif request.session["usuario_type"] == 'cuidacoches':
            return redirect('/home_cuidacoches/')

    else:
        form = ValidacionCuidacoches()
        mensaje = "Introduzca sus datos"
        if request.method == "POST":
            # Obtenemos los datos del formulario
            ci_form = request.POST.get('ci')
            reg_form = request.POST.get('num_registro')
            # Verificamos que el numero de registro existe
            try:
                dato_reg = Registro.objects.get(num_registro=int(reg_form))
                # Si el registro existe trae los datos
                if dato_reg:
                    if dato_reg.ci == int(ci_form):
                        redirige = '/save/{}/'.format(reg_form) 
                        return redirect(redirige)
                    else:
                        mensaje ="Su número de cédula no concuerda con el registro"
                        return render(request, "verificar_cuidacoches.html", {'form': form, 'mensaje': mensaje})
            # Se muestra si no encuentra el numero de registro
            except:
                mensaje = "El número de registro no es válido"
                return render(request, "verificar_cuidacoches.html", {'form': form, 'mensaje': mensaje})
        else:
            return render(request, "verificar_cuidacoches.html", {'form': form, 'mensaje': mensaje})


def save_register(request, num_registro):
    if "usuario_type" in request.session:

        if request.session["usuario_type"] == 'conductor':
            return redirect('/home_conductor/')
        
        elif request.session["usuario_type"] == 'cuidacoches':
            return redirect('/home_cuidacoches/')
    else:
        form = RegistroCuidacochesApp
        try:
            dato_reg = Registro.objects.get(num_registro=int(num_registro))
        except:
            pass
        if request.method == "POST":
    
            cant_lug_form = request.POST.get('cant_lugares')
            tel_form = request.POST.get('telefono')
            mail_form = request.POST.get('mail')
            num_banc_form = request.POST.get('cuenta_bancaria')
            banco_form = request.POST.get('banco')
            pass_form = request.POST.get('password')

            new_cuidacoches = Cuidacoches(
                nombre = dato_reg.nombre,
                apellido = dato_reg.apellido,
                ci = dato_reg.ci,
                num_registro = dato_reg.num_registro,
                direccion = dato_reg.direccion,
                nombre_trabajo = dato_reg.nombre_trabajo,
                latitud = dato_reg.latitud,
                longitud = dato_reg.longitud,
                horario_inicio = dato_reg.horario_inicio,
                horario_fin = dato_reg.horario_fin,
                telefono = int(tel_form),
                mail = mail_form,
                fecha_nacimiento = None,
                cuenta_bancaria = int(num_banc_form),
                banco = banco_form,
                promedio_calificacion = None,
                cantidad_votos = None,
                estado = True,
                cant_lugares = int(cant_lug_form),
                lugares_disponibles = int(cant_lug_form),
                password = pass_form
            )

            new_cuidacoches.save()
            new_monedero_cuidacoches = MonederoCuidacoches(ci = new_cuidacoches, monto = 0)
            new_monedero_cuidacoches.save()

            return redirect('/login_cuidacoches/')

        return render(request, "registro_cuidacoches.html", {'form': form, 'reg_imm': dato_reg})


def register_conductor(request):
    if "usuario_type" in request.session:
        if request.session["usuario_type"] == 'conductor':
            return redirect('/home_conductor/')
        elif request.session["usuario_type"] == 'cuidacoches':
            return redirect('/home_cuidacoches/')
    else:
        form = ConductorForm(request.POST)
        mensaje = 'Bienvenido, introduzca sus datos:'
        if request.method == "POST":
            if form.is_valid():
                new_conductor = form.save()
                new_monedero_conductor = MonederoConductor(ci = new_conductor, monto = 0)
                new_monedero_conductor.save()
                return redirect('/login_conductor/')
        else:
            form = ConductorForm()
        return render(request, 'pruebareg_cond.html', {'form': form, 'mensaje':mensaje})


def login_conductor(request):
    if "usuario_type" in request.session:
        if request.session["usuario_type"] == 'conductor':
            return redirect('/home_conductor/')
        elif request.session["usuario_type"] == 'cuidacoches':
            return redirect('/home_cuidacoches/')
    else:
        form = LoginForm()
        mensaje = 'Introduzca sus credenciales'
        tipo_usuario = 'conductor'
        if request.method == "POST":
            ci_form = request.POST.get('ci')
            pass_form = request.POST.get('password')
            try:
                dato_reg = Conductor.objects.get(ci=ci_form)

                if dato_reg:
                    if dato_reg.password == pass_form:
                        

                        request.session["usuario_ci"] = dato_reg.ci
                        request.session["usuario_type"] = 'conductor'

                        return redirect('/home_conductor/')
                        
                    else:
                        mensaje ="Su contraseña no coincide"
                        return render(request, "login.html", {'form': form, 'mensaje': mensaje, 'tipo_usuario': tipo_usuario})
            # Se muestra si no encuentra el numero de registro
            except:
                mensaje = "No existe un usuario registrado con esa ci"
                return render(request, "login.html", {'form': form, 'mensaje': mensaje, 'tipo_usuario': tipo_usuario})
        else:
            return render(request, "login.html", {'form': form, 'mensaje': mensaje, 'tipo_usuario': tipo_usuario})


def login_cuidacoches(request):
    if "usuario_type" in request.session:

        if request.session["usuario_type"] == 'conductor':
            return redirect('/home_conductor/')
        
        elif request.session["usuario_type"] == 'cuidacoches':
            return redirect('/home_cuidacoches/')

    else:

        form = LoginForm()
        mensaje = 'Introduzca sus credenciales'
        tipo_usuario = 'cuidacoches'
        if request.method == "POST":
            ci_form = request.POST.get('ci')
            pass_form = request.POST.get('password')
            try:
                dato_reg = Cuidacoches.objects.get(ci=ci_form)

                if dato_reg:
                    if dato_reg.password == pass_form:
                        

                        request.session["usuario_ci"] = dato_reg.ci
                        request.session["usuario_type"] = 'cuidacoches'

                        return redirect('/home_cuidacoches/')
                        
                    else:
                        mensaje ="Su contraseña no coincide"
                        return render(request, "login.html", {'form': form, 'mensaje': mensaje, 'tipo_usuario': tipo_usuario})
            # Se muestra si no encuentra el numero de registro
            except:
                mensaje = "No existe un usuario registrado con esa ci"
                return render(request, "login.html", {'form': form, 'mensaje': mensaje, 'tipo_usuario': tipo_usuario})
        else:
            return render(request, "login.html", {'form': form, 'mensaje': mensaje, 'tipo_usuario': tipo_usuario})


def logout(request):
    try:
        del request.session["usuario_ci"]
        del  request.session["usuario_type"]
    except KeyError:
        pass
    return redirect('/')


def home_cuidacoches(request):
    if "usuario_type" in request.session:
        if request.session["usuario_type"] == 'conductor':
            return redirect('/home_conductor/')
        
        elif request.session["usuario_type"] == 'cuidacoches':
            tipo = request.session["usuario_type"]
            mensaje = ''
            cuidacoches = Cuidacoches.objects.get(ci=int(request.session["usuario_ci"]))
            ocuparForm = OcuparForm()
            liberarForm = LiberarForm()
            lugaresOcupados = cuidacoches.cant_lugares - cuidacoches.lugares_disponibles
            
            if request.method == "POST":
                liberar = request.POST.get('liberar_espacio')
                ocupar = request.POST.get('ocupar_espacio')

                if liberar == '1':
                    if cuidacoches.lugares_disponibles < cuidacoches.cant_lugares:
                        cuidacoches.lugares_disponibles += 1
                    
                    cuidacoches.save()
                    lugaresOcupados = cuidacoches.cant_lugares - cuidacoches.lugares_disponibles

                    return render(request, "home_cuidacoches.html", {'tipo': tipo, 'lugOcupados': lugaresOcupados, 'OcuparForm':ocuparForm, 'LiberarForm': liberarForm, 'cuidacoches': cuidacoches, 'mensaje': mensaje}) 
            
                elif ocupar == '1':
                    if cuidacoches.lugares_disponibles > 0:
                        cuidacoches.lugares_disponibles -= 1
                    cuidacoches.save()
                    lugaresOcupados = cuidacoches.cant_lugares - cuidacoches.lugares_disponibles

                    return render(request, "home_cuidacoches.html", {'tipo': tipo, 'lugOcupados': lugaresOcupados, 'OcuparForm':ocuparForm, 'LiberarForm': liberarForm, 'cuidacoches': cuidacoches, 'mensaje': mensaje}) 
            

            return render(request, "home_cuidacoches.html", {'tipo': tipo, 'lugOcupados': lugaresOcupados, 'OcuparForm':ocuparForm, 'LiberarForm': liberarForm, 'cuidacoches': cuidacoches, 'mensaje': mensaje}) 
            

    else:
        return redirect('/')

    
def monedero_cuidacoches(request):
    if "usuario_type" in request.session:
        if request.session["usuario_type"] == 'conductor':
            return redirect('/home_conductor/')
        
        elif request.session["usuario_type"] == 'cuidacoches':
            cuidacoches = Cuidacoches.objects.get(ci=int(request.session["usuario_ci"]))
            monedero = MonederoCuidacoches.objects.get(ci=cuidacoches)
            tipo = request.session["usuario_type"]

            try:
                relaciones = Relacion.objects.filter(cuidacoches=cuidacoches).order_by('-fecha')

            except ValueError:
                relaciones = None
                
            
            return render(request, "monedero_cuidacoches.html", {'tipo': tipo, 'relaciones': relaciones, 'monedero': monedero, 'cuidacoches': cuidacoches}) 

    else:
        return redirect('/')


def perfil_cuidacoches(request):
    if "usuario_type" in request.session:
        if request.session["usuario_type"] == 'conductor':
            return redirect('/home_conductor/')
        
        elif request.session["usuario_type"] == 'cuidacoches':
            cuidacoches = Cuidacoches.objects.get(ci=int(request.session["usuario_ci"]))

            try:
                relaciones = Relacion.objects.filter(cuidacoches=cuidacoches).order_by('-fecha')

            except ValueError:
                relaciones = None

            return render(request, "perfil_cuidacoches.html", {'relaciones': relaciones, 'cuidacoches': cuidacoches}) 

    else:
        return redirect('/')



def home_conductor(request):
    if "usuario_type" in request.session:
        if request.session["usuario_type"] == 'cuidacoches':
            return redirect('/home_cuidacoches/')
        
        elif request.session["usuario_type"] == 'conductor':
            tipo = 'conductor'
        
            conductor = Conductor.objects.get(ci=int(request.session["usuario_ci"]))
            if conductor.notificacion == 0:

                if request.method == "POST":
                    
                    cuidacoches = Cuidacoches.objects.get(num_registro=int(request.POST.get('num_registro')))
                    relacion = Relacion(cuidacoches=cuidacoches, conductor=conductor)
                    relacion.save()
                    conductor.notificacion = relacion.id
                    conductor.save()

                    return redirect('/estacionado/')


                else:
                    coordenadas = Cuidacoches.objects.all()
                    return render(request, 'mapa.html', {'tipo': tipo, 'coordenadas': coordenadas})

            else:
                return redirect('/estacionado/')




    else:
        return redirect('/')

def estacionado(request):
    if "usuario_type" in request.session:
        if request.session["usuario_type"] == 'cuidacoches':
            return redirect('/home_cuidacoches/')
        
        elif request.session["usuario_type"] == 'conductor':
            tipo = 'conductor'
            conductor = Conductor.objects.get(ci=int(request.session["usuario_ci"]))
            if conductor.notificacion != 0:
                rel = Relacion.objects.get(id=conductor.notificacion)
                cuidacoches = rel.cuidacoches

                return render(request, 'estacionado.html', {'conductor': conductor, 'rel': rel, 'tipo': tipo})

            else:
                return redirect('/home_conductor/')

    else:
        return redirect('/')




def rel(request):
    if "usuario_type" in request.session:
        if request.session["usuario_type"] == 'cuidacoches':
            return redirect('/home_cuidacoches/')
        
        elif request.session["usuario_type"] == 'conductor':
            tipo = 'conductor'
            conductor = Conductor.objects.get(ci=int(request.session["usuario_ci"]))
            if conductor.notificacion != 0:
                rel = Relacion.objects.get(id=conductor.notificacion)
                cuidacoches = rel.cuidacoches
                monedero_cuidacoches = MonederoCuidacoches.objects.get(ci=cuidacoches)
                monedero_conductor = MonederoConductor.objects.get(ci=conductor)

                if request.method == "POST":
                    
                    if request.POST.get('propina') and int(request.POST.get('propina')) > monedero_conductor.monto:
                        mensaje = 'Solo tiene ${} en su monedero. Por favor, introduzca una propina menor'.format(monedero_conductor.monto)
                        return render(request, 'rel.html', {tipo: 'tipo', 'conductor': conductor, 'rel': rel, 'mensaje': mensaje})
                    else:
                        if request.POST.get('propina'):
                            rel.propina = int(request.POST.get('propina'))
                        if request.POST.get('calificacion'):
                            rel.calificacion = int(request.POST.get('calificacion'))
                        if request.POST.get('comentario'):
                            rel.comentario = request.POST.get('comentario')
                        rel.save()
                        conductor.notificacion = 0
                        conductor.save()
                        if request.POST.get('calificacion'):

                            if cuidacoches.cantidad_votos != None:
                                cuidacoches.promedio_calificacion = ((cuidacoches.promedio_calificacion * cuidacoches.cantidad_votos) + int(request.POST.get('calificacion'))) / (cuidacoches.cantidad_votos + 1)
                                cuidacoches.cantidad_votos += 1
                            else:
                                cuidacoches.promedio_calificacion = int(request.POST.get('calificacion'))
                                cuidacoches.cantidad_votos = 1
                            
                            cuidacoches.save()
                        
                        if request.POST.get('propina') and int(request.POST.get('propina')) != 0:
                            monedero_conductor.monto -= int(request.POST.get('propina'))
                            monedero_cuidacoches.monto += int(request.POST.get('propina'))
                            monedero_conductor.save()
                            monedero_cuidacoches.save()

                        return redirect('/home_conductor/')




                else:
                    return render(request, 'rel.html', {tipo: 'tipo', 'conductor': conductor, 'rel': rel})

            else:
                return redirect('/home_conductor/')

    else:
        return redirect('/')


def servicios_conductor(request):
    if "usuario_type" in request.session:
        if request.session["usuario_type"] == 'cuidacoches':
            return redirect('/home_cuidacoches/')
        
        elif request.session["usuario_type"] == 'conductor':
            tipo = 'conductor'
        
            conductor = Conductor.objects.get(ci=int(request.session["usuario_ci"]))
            monedero = monedero_conductor = MonederoConductor.objects.get(ci=conductor)
            if conductor.notificacion == 0:
                
                try:
                    relaciones = Relacion.objects.filter(conductor=conductor).order_by('-fecha')

                except ValueError:
                    relaciones = None

                return render(request, "perfil_conductor.html", {'tipo' : tipo , 'relaciones': relaciones, 'conductor': conductor, 'monedero': monedero}) 
                

            else:
                return redirect('/estacionado/')

    else:
        return redirect('/')

def quienes_somos(request):
    return render(request, 'quienes_somos.html')

def como_funciona(request):
    return render(request, 'acerca_de.html')