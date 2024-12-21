import { PrismaClient } from '@prisma/client'
const prisma = new PrismaClient();
export async function GetUserByWhere(query : Object){
    const user = await prisma.user.findFirst({
        select:{
            id:true,
            role: true,
            username: true
        },
        where: query
    })
    return user
}