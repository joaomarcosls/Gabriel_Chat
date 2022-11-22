from robo import *
import unittest

class TestSaudacoes(unittest.TestCase):
    def setUp(self):
        self.robo = iniciar()

    def test_01_oi_ola_tudobem(self):
        saudacoes = ["oi", "olá", "tudo bem?"]

        for saudacao in saudacoes:
            print(f"testando saudação: {saudacao}")

            resposta = self.robo.get_response(saudacao.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Olá, sou o robô de atendimento Gabriel. Como posso te ajudar?", 
                resposta.text
            )

    def test_02_bomdia_boatarde_boanoite(self):
        saudacoes = ["Bom dia", "Boa tarde", "Boa noite"]

        for saudacao in saudacoes:
            print(f"testando saudação: {saudacao}")
 
            resposta = self.robo.get_response(saudacao.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                saudacao + ", sou o robô de atendimento Gabriel. Como posso te ajudar?",
                resposta.text
            )


if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TestSaudacoes))

    exec = unittest.TextTestRunner()
    exec.run(testes)