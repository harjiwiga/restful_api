"""empty message

Revision ID: e95afac53d07
Revises: a5f20a2f4d26
Create Date: 2019-02-04 02:05:26.669462

"""
from alembic import op
import sqlalchemy as sa
from geoalchemy2.types import Geometry


# revision identifiers, used by Alembic.
revision = 'e95afac53d07'
down_revision = 'a5f20a2f4d26'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('report_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('user_type_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_type_id'], ['user_type.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('report',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('report_type_id', sa.Integer(), nullable=True),
    sa.Column('report_time', sa.DateTime(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('address', sa.String(length=120), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('radius', sa.Float(), nullable=True),
    sa.Column('reporter_id', sa.Integer(), nullable=True),
    sa.Column('update_status_time', sa.DateTime(), nullable=False),
    sa.Column('location', Geometry(geometry_type='POINT'), nullable=True),
    sa.Column('description', sa.String(length=300), nullable=True),
    sa.Column('picture_url', sa.String(length=300), nullable=True),
    sa.ForeignKeyConstraint(['report_type_id'], ['report_type.id'], ),
    sa.ForeignKeyConstraint(['reporter_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['status'], ['status.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('token_blacklist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jti', sa.String(length=36), nullable=False),
    sa.Column('token_type', sa.String(length=10), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('revoked', sa.Boolean(), nullable=False),
    sa.Column('expires', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('jti')
    )
    op.create_table('users_roles',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('report_voter_table',
    sa.Column('report_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['report_id'], ['report.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    # op.drop_table('spatial_ref_sys')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('spatial_ref_sys',
    sa.Column('srid', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('auth_name', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('auth_srid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('srtext', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.Column('proj4text', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.CheckConstraint('(srid > 0) AND (srid <= 998999)', name='spatial_ref_sys_srid_check'),
    sa.PrimaryKeyConstraint('srid', name='spatial_ref_sys_pkey')
    )
    op.drop_table('report_voter_table')
    op.drop_table('users_roles')
    op.drop_table('token_blacklist')
    op.drop_table('report')
    op.drop_table('user')
    op.drop_table('user_type')
    op.drop_table('status')
    op.drop_table('role')
    op.drop_table('report_type')
    # ### end Alembic commands ###
