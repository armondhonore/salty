#user_billygoat:
#  user.present:
#    - name: billygoat
#    - fullname: Billy Gaot
#    - shell: /bin/bash
#    - home: /home/billygoat
#    - uid: 10000
#    - gid_from_name: True

{% for user, data in pillar.get('system_users', {}).items() %}
user_{{ user }}:
  user.present:
    - name: {{ user }}
    - fullname: {{ data['fullname'] }}
    - shell: /bin/bash
    - home: /home/{{ user }}
    - uid: {{ data['uid'] }}
    - gid_from_name: True
    - groups: []

{% endfor %}
