from flask import render_template, redirect, url_for, flash, session
from datetime import datetime
from app.main.forms import NameForm
from app.models import User, Role, db
from app.main import bp as main

@main.route('/')
def index():
    current_time = datetime.utcnow()
    return render_template('index.html', current_time=current_time)

@main.route('/professores')
def professores():
    return render_template('indisponivel.html')

@main.route('/disciplinas')
def disciplinas():
    return render_template('indisponivel.html')

@main.route('/cursos')
def cursos():
    return render_template('indisponivel.html')

@main.route('/alunos')
def alunos():
    return render_template('indisponivel.html')


# ATENÇÃO PARA ALTERAR O NOME DE VERIFICAÇÃO
@main.route('/ocorrencias', methods=['GET', 'POST'])
def ocorrencias():
    form = NameForm()

    if form.validate_on_submit():
        name = form.name.data
        disciplina = form.disciplina.data
        existing_user = User.query.filter_by(username=name).first()

        if existing_user is None:
            # Cria um novo professor
            new_user = User(username=name)

            # Verifica se a role (disciplina) existe no banco de dados
            user_role = Role.query.filter_by(name=disciplina).first()

            # Se a role não existir, cria uma nova role (disciplina)
            if user_role is None:
                user_role = Role(name=disciplina)
                db.session.add(user_role)
                db.session.commit()

            # Associa a role ao usuário
            new_user.role = user_role

            # Adiciona o novo professor no banco de dados
            db.session.add(new_user)
            db.session.commit()

            flash('Ocorrência cadastrada com sucesso!', 'success')
            session['user_exists'] = False
        else:
            # Se o professor já existe
            flash('A ocorrência já existe!', 'warning')
            session['user_exists'] = True

        # Armazena o nome na sessão e redireciona de volta para a página de professores
        session['name'] = name
        return redirect(url_for('main.ocorrencias'))

    # Para exibir o formulário e a lista de professores cadastrados
    name = session.get('name', None)
    users = User.query.all()
    return render_template('cadastro_ocorrencia.html', form=form, users=users, name=name)


@main.route('/limpar_banco_de_dados')
def limpar_banco_de_dados():
    try:
        # Excluir todos os registros da tabela 'User'
        db.session.query(User).delete()

        # Excluir todos os registros da tabela 'Role'
        db.session.query(Role).delete()

        # Confirmar as mudanças no banco de dados
        db.session.commit()

        return "Banco de dados limpo com sucesso!"

    except Exception as e:
        # Caso haja erro, fazer rollback e retornar erro
        db.session.rollback()
        return f"Erro ao limpar o banco de dados: {str(e)}"






