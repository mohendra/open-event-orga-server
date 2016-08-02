"""empty message

Revision ID: d01ead213e8e
Revises: 291bb44bb014
Create Date: 2016-07-31 10:08:38.145030

"""

# revision identifiers, used by Alembic.
revision = 'd01ead213e8e'
down_revision = '291bb44bb014'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('identifier', sa.String(), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('country', sa.String(), nullable=True),
    sa.Column('zipcode', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('completed_at', sa.DateTime(), nullable=True),
    sa.Column('transaction_id', sa.String(), nullable=True),
    sa.Column('paid_via', sa.String(), nullable=True),
    sa.Column('payment_mode', sa.String(), nullable=True),
    sa.Column('brand', sa.String(), nullable=True),
    sa.Column('exp_month', sa.Integer(), nullable=True),
    sa.Column('exp_year', sa.Integer(), nullable=True),
    sa.Column('last4', sa.String(), nullable=True),
    sa.Column('token', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('identifier')
    )
    op.create_table('tax',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('country', sa.String(), nullable=True),
    sa.Column('tax_name', sa.String(), nullable=False),
    sa.Column('tax_rate', sa.Float(), nullable=False),
    sa.Column('tax_id', sa.String(), nullable=False),
    sa.Column('send_invoice', sa.Boolean(), nullable=True),
    sa.Column('registered_company', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('zip', sa.Integer(), nullable=True),
    sa.Column('invoice_footer', sa.String(), nullable=True),
    sa.Column('tax_include_in_price', sa.Boolean(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orders_tickets',
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('ticket_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
    sa.ForeignKeyConstraint(['ticket_id'], ['ticket.id'], ),
    sa.PrimaryKeyConstraint('order_id', 'ticket_id')
    )
    op.create_table('ticket_holders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('country', sa.String(), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'settings', sa.Column('stripe_publishable_key', sa.String(), nullable=True))
    op.add_column(u'settings', sa.Column('stripe_secret_key', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'settings', 'stripe_secret_key')
    op.drop_column(u'settings', 'stripe_publishable_key')
    op.drop_table('ticket_holders')
    op.drop_table('orders_tickets')
    op.drop_table('tax')
    op.drop_table('orders')
    ### end Alembic commands ###