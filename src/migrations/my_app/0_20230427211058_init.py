from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `users` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `vk_id` INT NOT NULL UNIQUE,
    `name` LONGTEXT NOT NULL,
    `level` INT NOT NULL  DEFAULT 1,
    `exp` INT NOT NULL  DEFAULT 0,
    `date_reg` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6)
) CHARACTER SET utf8mb4 COMMENT='Модель пользователя';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
