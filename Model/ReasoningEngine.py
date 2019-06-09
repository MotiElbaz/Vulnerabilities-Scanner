from threading import Lock


class ReasoningEngine(object):
    _instance = None

    def getPrivPre(self, desc, impact, privReq='', auth=''):
        # Provides
        vocabulary1 = ['gain root', 'gain unrestricted', 'root shell access’', 'obtain root']
        vocabulary2 = ['gain privilege', 'gain host OS privilege', 'gain admin', 'obtain local admin',
                       'obtain admin', 'gain unauthorized access', 'to root', 'to the root',
                       'elevate the privilege', 'elevate privilege', 'root privileges via buffer overflow']
        vocabulary34 = ['unspecified vulnerability', 'unspecified other impact', 'unspecified impact', 'other impacts']
        vocabulary5 = ['gain privilege', 'gain unauthorized access']
        vocabulary6 = ['gain admin', 'obtain admin']
        vocabulary7 = ['hijack the authentication of admin', 'hijack the authentication of super admin',
                       'hijack the authentication of moderator' ]
        vocabulary8 = ['hijack the authentication of users', 'hijack the authentication of arbitrary users',
                       'hijack the authentication of unspecified victims']
        vocabulary91011 = ['obtain password', 'obtain credential', 'sniff ... credentials',
                           'sniff ... passwords', 'steal ... credentials', 'steal ... passwords']
        vocabulary121314 = ['cleartext credential', 'cleartext password', 'obtain plaintext', 'obtain cleartext',
                            'discover cleartext', 'read network traffic', 'un-encrypted',  'unencrypted',
                            'intercept transmission', 'intercept communication', 'obtain and decrypt passwords',
                            'conduct offline password guessing', 'bypass authentication']
        vocabulary1516 = ['buffer overflow', 'command injection', 'write arbitrary,file', 'command execution',
                          'execute command', 'execute root command', 'execute commands as root',
                          'execute arbitrary', 'execute dangerous', 'execute php', 'execute script', 'execute local',
                          'execution of arbitrary', 'execution of command', 'remote execution', 'execute code',
                          'execute arbitrary SQL']
        vocabulary17 = ['SQL injection']
        vocabulary18 = ['']
        vocabulary = [vocabulary1, vocabulary2, vocabulary34, vocabulary34, vocabulary5, vocabulary6, vocabulary7, vocabulary8,
                      vocabulary91011, vocabulary91011, vocabulary91011, vocabulary121314, vocabulary121314, vocabulary121314, vocabulary1516,
                      vocabulary1516, vocabulary17, vocabulary18]
        impacts = ['Complete', 'Complete', 'Complete', 'Partial', 'Partial', 'Partial', '', '', 'Complete',
                   'Partial', 'Partial', 'Complete', 'Partial', 'Partial', 'Complete', 'Partial', '', 'Any None']
        pres = ['sys_root_priv', 'sys_root_priv', 'sys_root_priv', 'sys_user_priv', 'sys_user_priv', 'app_admin_priv',
                'app_admin_priv', 'app_user_priv', 'sys_root_priv', 'sys_user_priv', 'app_admin_priv', 'sys_root_priv',
                'sys_user_priv', 'app_admin_priv', 'sys_root_priv', 'sys_user_priv', 'app_admin_priv', 'None']
        # for v, i, p in vocabulary, impacts, pres:
        #     for word in v:
        #         if word in desc and impact == i:
        #             return p
        impact = impact.lower()
        desc = desc.lower()
        for i in range(18):
            for sentence in vocabulary[i]:
                imp = impacts[i]
                if sentence.lower() in desc and impact == impacts[i].lower():
                    return pres[i]

        # if 'sniff' in desc and 'credentials' in desc and impact == 'complete':
        #     return 'sys_root_priv'
        # if 'sniff' in desc and 'passwords' in desc and impact == 'complete':
        #     return 'sys_root_priv'
        # if 'steal' in desc and 'credentials' in desc and impact == 'complete':
        #     return 'sys_root_priv'
        # if 'steal' in desc and 'passwords' in desc and impact == 'complete':
        #     return 'sys_root_priv'
        # if 'sniff' in desc and 'credentials' in desc and impact == 'partial':
        #     return 'sys_root_priv'
        # if 'sniff' in desc and 'passwords' in desc and impact == 'partial':
        #     return 'sys_root_priv'
        # if 'steal' in desc and 'credentials' in desc and impact == 'partial':
        #     return 'sys_root_priv'
        # if 'steal' in desc and 'passwords' in desc and impact == 'partial':
        #     return 'sys_root_priv'

        privReq = privReq.lower()
        if privReq == 'none':
            return 'app_user_priv'
        if privReq == 'app_user_priv':
            return 'app_admin_priv'
        if privReq == 'app_admin_priv':
            return 'sys_user_priv'
        if privReq == 'sys_user_priv':
            return 'sys_root_priv'


    def getPrivPost(self, desc, av, auth='', priv=''):
        # Requires
        vocabulary1 = ['allows local users', 'allowing local users', 'allow local users', 'allows the local user']
        vocabulary2 = ['allows local administrators', 'allow local administrators', 'allows the local administrator']
        vocabulary3 = ['authenticated user', 'remote authenticated users with administrative privileges']
        vocabulary4 = ['remote authenticated admin', 'remote authenticated users with administrative privileges']
        vocabulary5 = ['remote authenticated users']
        vocabulary6 = ['remote authenticated admin']
        vocabulary = [vocabulary1, vocabulary2, vocabulary3, vocabulary4, vocabulary5, vocabulary6]
        posts = ['sys_user_priv', 'sys_root_priv', 'app_user_priv', 'app_admin_priv', 'sys_user_priv', 'sys_root_priv']

        # for v, p in  vocabulary, posts:
        #     for word in v:
        #         if word in desc:
        #             return p

        for i in range(6):
            for sentence in vocabulary[i]:
                if sentence.lower() in desc.lower():
                    return posts[i]

        av = av.lower()
        auth = auth.lower()
        priv = priv.lower()
        if auth == '':
            if av == '' and priv == 'none':
                return 'None'
            if av == 'local' and priv == 'none':
                return 'None'
            if av != 'local' and priv == 'none':
                return 'None'
            if av == 'local' and priv == 'low':
                return 'sys_user_priv'
            if av == 'local' and priv == 'high':
                return 'sys_root_priv'
            if av != 'local' and priv == 'low':
                return 'app_user_priv'
            if av != 'local' and priv == 'high':
                return 'app_admin_priv'

        if priv == '':
            if av == '' and auth == '':
                return 'None'
            if av == 'local' and auth == '':
                return 'sys_user_priv'
            if av == 'local' and auth != 'none':
                return 'sys_root_priv'
            if av == 'local' and auth == 'none':
                return 'sys_user_priv'
            if av != 'local' and auth != 'none':
                return 'app_admin_priv'
            if av != 'local' and auth == 'none':
                return 'app_user_priv'
            if av != 'local' and auth == '':
                return 'app_user_priv'


    def __new__(cls, *args, **kwargs):
        if ReasoningEngine._instance is None:
            with Lock():
                if ReasoningEngine._instance is None:
                    ReasoningEngine._instance = super().__new__(cls, *args, **kwargs)

        return ReasoningEngine._instance
