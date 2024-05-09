from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from etablissement.models import Etudiant

import qrcode
import cv2

from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
# Create your views here.


@login_required(login_url='login')
def generer_code(request, id):
    """ Vue permettant de générer le code QR """
    etudiant = get_object_or_404(Etudiant, pk=id)
    
    # Donnée du code QR
    data = etudiant.id
    
    
    # Génération du code QR
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    
    # Image du code QR
    qr_image = qr.make_image(fill_color="black", back_color="white")
    
    # Réponse HTTP du téléchargement de l'image
    response = HttpResponse(content_type="image/png")
    qr_image.save(response, "PNG")
    response['Content-Disposition'] = f'attachment; filename="{etudiant.full_name}_{etudiant.promotion.name}qr_code.png"'

    return response



@login_required(login_url='login')
def dechiffrer(request):
    """ Dechiffrer le code provenant du QR """
    user = request.user
    
    etudiants = Etudiant.objects.all()
    
    decision = ''
    message = "Etudiant introuvable !"
        
    if request.method == 'POST':
        """ Verifier si la methode est POST """
        # Récupère la donnée du formulaire
        code  = request.POST.get('code')
        
        for etudiant in etudiants:
            if code == str(etudiant.id):
                return redirect('detail_etudiant', id=etudiant.id)
        
        decision = 1

    return render(request, 'qr_app/dechiffre.html', {'user': user, 'decision': decision, 'message': message})



@login_required(login_url="login")
def lire_code_qr(request):
    etudiants = Etudiant.objects.all()

    # Ouvrir la caméra
    cap = cv2.VideoCapture(0)

    while True:
        # Capturer une image à partir de la caméra
        ret, frame = cap.read()

        # Vérifier si la capture d'image a réussi
        if not ret:
            break

        # Décoder le code QR dans l'image
        detector = cv2.QRCodeDetector()
        data, bbox, straight_qrcode = detector.detectAndDecode(frame)

        # Si un code QR est détecté, extraire l'identifiant de l'étudiant
        if data:
            try:
                for etudiant in etudiants:
                    if data == str(etudiant.id):
                        # Fermer toutes les fenêtres ouvertes par OpenCV
                        cv2.destroyAllWindows()
                        # Libérer la caméra
                        cap.release()
                        # Rediriger vers la page de détail de l'étudiant
                        return redirect('detail_etudiant', id=etudiant.id)

            except ValueError:
                # Si l'identifiant n'est pas un entier, afficher un message d'erreur
                return render(request, 'qr_code_reader.html', {'error_message': 'Le code QR ne contient pas un identifiant valide.'})

        # Afficher l'image de la caméra
        cv2.imshow('frame', frame)

        # Vérifier si l'utilisateur a appuyé sur la touche 'q' pour quitter
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libérer la caméra
    cap.release()

    # Fermer toutes les fenêtres ouvertes par OpenCV
    cv2.destroyAllWindows()

    # Rediriger vers la page de lecture de code QR
    return redirect('decode')



def scan_qr_code(request):
    etudiants = Etudiant.objects.all()
    
    if request.method == 'POST':
        code = request.POST.get('code')
        print(code)
        try:
            for etudiant in etudiants:
                if code == str(etudiant.id):
                    # Rediriger vers la fiche d'identification de l'étudiant
                    return redirect('detail_etudiant', id=etudiant.id)
                
        except ValueError:
            return JsonResponse({'error': 'Le code QR n\'est pas valide.'}, status=400)

    return render(request, 'qr_app/scan.html')