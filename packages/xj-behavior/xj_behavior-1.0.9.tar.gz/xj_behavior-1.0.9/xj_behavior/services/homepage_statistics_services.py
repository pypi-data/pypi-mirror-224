from orator import DatabaseManager
from decimal import Decimal
from config.config import JConfig
from xj_enroll.api.enroll_apis import EnrollAPI
from xj_enroll.service.enroll_record_serivce import EnrollRecordServices
from xj_finance.services.finance_transacts_service import FinanceTransactsService
from xj_role.services.user_group_service import UserGroupService
from xj_user.services.user_relate_service import UserRelateToUserService
from ..utils.custom_tool import force_transform_type
from ..utils.join_list import JoinList

config = JConfig()
db_config = {
    config.get('main', 'driver', "mysql"): {
        'driver': config.get('main', 'driver', "mysql"),
        'host': config.get('main', 'mysql_host', "127.0.0.1"),
        'database': config.get('main', 'mysql_database', ""),
        'user': config.get('main', 'mysql_user', "root"),
        'password': config.get('main', 'mysql_password', "123456"),
        "port": config.getint('main', 'mysql_port', "3306")
    }
}
db = DatabaseManager(db_config)


class HomepageStatisticsServices():
    @staticmethod
    def statistics(params: dict = None):
        deal_orders = db.table('enroll_enroll').where_in('enroll_status_code', [80, 668]).count()
        number_escorters = db.table(db.raw(f"role_user_to_role as r1")).left_join(db.raw(f"role_role as r2"),
                                                                                  'r1.role_id',
                                                                                  '=', 'r2.id').where_in('role',
                                                                                                         ['BX-WORKER',
                                                                                                          'CASUAL_WORKER']).count()
        bid_winning_amount = db.table('thread').sum('field_2')

        statistics = {
            'deal_orders': deal_orders,
            'number_escorters': number_escorters,
            'bid_winning_amount': bid_winning_amount if bid_winning_amount else Decimal('0.0')
        }
        return statistics, None
