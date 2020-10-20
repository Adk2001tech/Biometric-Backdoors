# Biometric-Backdoors


## ABSTRACT

<hr>

* In recent years, biometric authentication has become one of the
preferred ways to mitigate burdens associated with passwords. With
a long history of research, face and fingerprint recognition are
the most popular modalities and authentication systems based on
them are commonly delivered with consumer products. 


<img align="right" src="Images/ABSTRACT.png" width="480" title="Mask-RCNN Model">



* While early research focused on the performance of these modalities under a
zero-effort threat model, current trends in biometric systems are
also prioritizing high protection of biometric templates, i.e., the
users stored biometric information. Templates in fact represent
sensitive user data and their leak might compromise the secrecy of
the biometric trait in a permanent way.

* **An adversary(Attacker) can exploit the template update procedure to cause the system to adapt the template, thereby indirectly modifying the data within. In fact, during template update, the system replaces or adds recently seen samples to the user template. In this attack, the adversary corrupts the user template allowing himself to impersonate the user with his own biometric trait. The poisoned template is hard to detectand creates an inconspicuous and stealthy backdoor for the adversary in the long-term. Once placed, the backdoor allows the adversary to access the system without requiring them to modify their appearance.**

## Contributions to Repository

1. Introduction towards Face recognition systems.
2. Adversarial ML Attacks.
3. Poisoning Sample Generation.
4. Poisoning Attack Injection.
5. Evaluation Techniques for Adversarial ML Attacks.















<a href="https://github.com/Adk2001tech/Biometric-Backdoors/blob/main/Notebooks/Face_Detection_basic.ipynb">Link1</a>

Basic Introduction towards Face Detection Algorithm


<a href="https://github.com/Adk2001tech/Biometric-Backdoors/blob/main/Notebooks/Biometric_Backdoors_Part1_INTRO.ipynb">Link2</a>

Project Overview

<a href="https://github.com/Adk2001tech/Biometric-Backdoors/blob/main/Notebooks/Poisoning%20Samples%20Generation%20Part(2.1)%20CENTROID.ipynb">Link3</a>

**Poisoning Sample Generation**: Centroid Shifting 


<a href="https://github.com/Adk2001tech/Biometric-Backdoors/blob/main/Notebooks/Poisoning%20Samples%20Generation%20Part(2.2)%20Target.ipynb">Link4</a>

**Poisoning Sample Generation**: Target shifting
