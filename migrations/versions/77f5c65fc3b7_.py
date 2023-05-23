"""empty message

Revision ID: 77f5c65fc3b7
Revises: 22160caed3ca
Create Date: 2023-05-06 15:40:11.701408

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77f5c65fc3b7'
down_revision = '22160caed3ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_link', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('text', sa.UnicodeText(length=1000), nullable=False))
        batch_op.drop_column('question_image_link')
        batch_op.drop_column('question_text')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('question_text', sa.TEXT(length=1000), nullable=False))
        batch_op.add_column(sa.Column('question_image_link', sa.TEXT(), nullable=True))
        batch_op.drop_column('text')
        batch_op.drop_column('image_link')

    # ### end Alembic commands ###